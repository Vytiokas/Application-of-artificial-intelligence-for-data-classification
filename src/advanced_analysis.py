"""
Išplėstinė analizė su papildomomis funkcijomis:
- Cross-validation
- Feature importance
- ROC kreivės
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import roc_curve, auc, roc_auc_score
import warnings
import os

warnings.filterwarnings('ignore')
os.makedirs('results', exist_ok=True)


def cross_validation_analysis(X, y):
    """
    Atlikti kryžminį validavimą visiems modeliams
    """
    print("\n" + "=" * 70)
    print("KRYŽMINIS VALIDAVIMAS (5-Fold Cross-Validation)")
    print("=" * 70)
    
    # Standartizavimas
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    models = {
        'Logistic Regression': LogisticRegression(max_iter=10000, random_state=42),
        'Decision Tree': DecisionTreeClassifier(random_state=42, max_depth=5),
        'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
        'SVM': SVC(kernel='rbf', random_state=42)
    }
    
    cv_results = []
    
    for name, model in models.items():
        scores = cross_val_score(model, X_scaled, y, cv=5, scoring='f1')
        cv_results.append({
            'Model': name,
            'Mean F1': scores.mean(),
            'Std F1': scores.std(),
            'Scores': scores
        })
        print(f"\n{name}:")
        print(f"  F1-Score: {scores.mean():.4f} (+/- {scores.std():.4f})")
        print(f"  Visi rezultatai: {[f'{s:.4f}' for s in scores]}")
    
    return cv_results


def plot_feature_importance(X, y, feature_names):
    """
    Vizualizuoti požymių svarbą Random Forest modelyje
    """
    print("\n" + "=" * 70)
    print("POŽYMIŲ SVARBA (Feature Importance)")
    print("=" * 70)
    
    # Paruošti duomenis
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Apmokyti Random Forest
    rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_model.fit(X_scaled, y)
    
    # Gauti požymių svarbą
    importances = rf_model.feature_importances_
    indices = np.argsort(importances)[::-1]
    
    # Spausdinti top 10
    print("\nTop 10 svarbiausių požymių:")
    for i in range(10):
        idx = indices[i]
        print(f"  {i+1}. {feature_names[idx]}: {importances[idx]:.4f}")
    
    # Vizualizacija
    plt.figure(figsize=(12, 8))
    top_n = 15
    top_indices = indices[:top_n]
    
    plt.barh(range(top_n), importances[top_indices], color='steelblue', alpha=0.7)
    plt.yticks(range(top_n), [feature_names[i] for i in top_indices])
    plt.xlabel('Svarba', fontsize=12)
    plt.title('Top 15 Svarbiausių Požymių (Random Forest)', 
             fontsize=14, fontweight='bold')
    plt.gca().invert_yaxis()
    plt.grid(axis='x', alpha=0.3)
    plt.tight_layout()
    plt.savefig('results/feature_importance.png', dpi=300, bbox_inches='tight')
    print("\n✓ Požymių svarbos grafikas išsaugotas: results/feature_importance.png")


def plot_roc_curves(X, y):
    """
    Nubraižyti ROC kreives visiems modeliams
    """
    print("\n" + "=" * 70)
    print("ROC KREIVĖS (Receiver Operating Characteristic)")
    print("=" * 70)
    
    # Paruošti duomenis
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Modeliai su probability support
    models = {
        'Logistic Regression': LogisticRegression(max_iter=10000, random_state=42),
        'Decision Tree': DecisionTreeClassifier(random_state=42, max_depth=5),
        'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
        'SVM': SVC(kernel='rbf', probability=True, random_state=42)
    }
    
    plt.figure(figsize=(10, 8))
    colors = ['#3498db', '#e74c3c', '#2ecc71', '#f39c12']
    
    for (name, model), color in zip(models.items(), colors):
        # Apmokyti modelį
        model.fit(X_train_scaled, y_train)
        
        # Gauti tikimybes
        if hasattr(model, "predict_proba"):
            y_proba = model.predict_proba(X_test_scaled)[:, 1]
        else:
            y_proba = model.decision_function(X_test_scaled)
        
        # Apskaičiuoti ROC kreivę
        fpr, tpr, _ = roc_curve(y_test, y_proba)
        roc_auc = auc(fpr, tpr)
        
        # Nubraižyti
        plt.plot(fpr, tpr, color=color, lw=2, 
                label=f'{name} (AUC = {roc_auc:.4f})')
        
        print(f"\n{name}:")
        print(f"  AUC Score: {roc_auc:.4f}")
    
    # Diagonalė (atsitiktinis klasifikatorius)
    plt.plot([0, 1], [0, 1], 'k--', lw=2, label='Atsitiktinis (AUC = 0.5000)')
    
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate', fontsize=12)
    plt.ylabel('True Positive Rate', fontsize=12)
    plt.title('ROC Kreivės Palyginimas', fontsize=14, fontweight='bold')
    plt.legend(loc="lower right", fontsize=10)
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig('results/roc_curves.png', dpi=300, bbox_inches='tight')
    print("\n✓ ROC kreivių grafikas išsaugotas: results/roc_curves.png")


def main():
    """
    Pagrindinė funkcija išplėstinei analizei
    """
    print("\n" + "=" * 70)
    print("IŠPLĖSTINĖ ANALIZĖ")
    print("=" * 70)
    
    # Įkelti duomenis
    data = load_breast_cancer()
    X = pd.DataFrame(data.data, columns=data.feature_names)
    y = pd.Series(data.target)
    
    # 1. Kryžminis validavimas
    cv_results = cross_validation_analysis(X, y)
    
    # 2. Požymių svarba
    plot_feature_importance(X, y, data.feature_names)
    
    # 3. ROC kreivės
    plot_roc_curves(X, y)
    
    print("\n" + "=" * 70)
    print("IŠPLĖSTINĖ ANALIZĖ BAIGTA!")
    print("=" * 70)


if __name__ == "__main__":
    main()
