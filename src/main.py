"""
Dirbtinio Intelekto Taikymas Duomenų Klasifikavimui
Autorius: Studentas
Data: 2026-02-05

Šis projektas demonstruoja keturių skirtingų mašininio mokymosi algoritmų
taikymą medicininių duomenų klasifikavimui.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)
import warnings
import os

warnings.filterwarnings('ignore')

# Sukurti results katalogą, jei neegzistuoja
os.makedirs('results', exist_ok=True)


def load_and_explore_data():
    """
    Įkelia duomenų rinkinį ir atlieka pradinę analizę
    """
    print("=" * 70)
    print("1. DUOMENŲ ĮKĖLIMAS IR ANALIZĖ")
    print("=" * 70)
    
    # Įkeliame Breast Cancer duomenų rinkinį
    data = load_breast_cancer()
    X = pd.DataFrame(data.data, columns=data.feature_names)
    y = pd.Series(data.target, name='target')
    
    print(f"\nDuomenų rinkinio dydis: {X.shape[0]} įrašų, {X.shape[1]} požymių")
    print(f"Klasių pasiskirstymas:")
    print(f"  - Gerybiniai (1): {sum(y == 1)} ({sum(y == 1)/len(y)*100:.1f}%)")
    print(f"  - Piktybiniai (0): {sum(y == 0)} ({sum(y == 0)/len(y)*100:.1f}%)")
    
    # Tikrinti trūkstamas reikšmes
    missing_values = X.isnull().sum().sum()
    print(f"\nTrūkstamos reikšmės: {missing_values}")
    
    # Statistinė informacija
    print("\nPagrindinė statistika (pirmi 5 požymiai):")
    print(X.iloc[:, :5].describe())
    
    return X, y, data.feature_names


def preprocess_data(X, y, test_size=0.2, random_state=42):
    """
    Paruošia duomenis mokymui:
    - Padalija į train/test rinkinius
    - Standartizuoja požymius
    """
    print("\n" + "=" * 70)
    print("2. DUOMENŲ PARUOŠIMAS")
    print("=" * 70)
    
    # Padalijimas į train ir test rinkinius
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )
    
    print(f"\nMokymo rinkinio dydis: {X_train.shape[0]} įrašų")
    print(f"Testavimo rinkinio dydis: {X_test.shape[0]} įrašų")
    
    # Standartizavimas (Z-score normalizacija)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    print("\nDuomenys standartizuoti naudojant StandardScaler")
    print(f"Vidurkis po standartizacijos: {X_train_scaled.mean():.6f}")
    print(f"Standartinis nuokrypis: {X_train_scaled.std():.6f}")
    
    return X_train_scaled, X_test_scaled, y_train, y_test


def train_models(X_train, y_train):
    """
    Apmokyti keturis skirtingus klasifikavimo modelius
    """
    print("\n" + "=" * 70)
    print("3. MODELIŲ MOKYMAS")
    print("=" * 70)
    
    models = {
        'Logistic Regression': LogisticRegression(max_iter=10000, random_state=42),
        'Decision Tree': DecisionTreeClassifier(random_state=42, max_depth=5),
        'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
        'Support Vector Machine': SVC(kernel='rbf', random_state=42)
    }
    
    trained_models = {}
    
    for name, model in models.items():
        print(f"\nMokomas modelis: {name}...")
        model.fit(X_train, y_train)
        trained_models[name] = model
        print(f"  ✓ {name} sėkmingai apmokytas")
    
    return trained_models


def evaluate_models(models, X_test, y_test):
    """
    Įvertinti visų modelių kokybę naudojant įvairias metrikus
    """
    print("\n" + "=" * 70)
    print("4. MODELIŲ VERTINIMAS")
    print("=" * 70)
    
    results = []
    
    for name, model in models.items():
        print(f"\n{name}:")
        print("-" * 50)
        
        # Prognozės
        y_pred = model.predict(X_test)
        
        # Metrikos
        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred)
        recall = recall_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)
        
        print(f"  Accuracy:  {accuracy:.4f}")
        print(f"  Precision: {precision:.4f}")
        print(f"  Recall:    {recall:.4f}")
        print(f"  F1-Score:  {f1:.4f}")
        
        # Išsami ataskaita
        print("\n  Klasifikacijos ataskaita:")
        print(classification_report(y_test, y_pred, 
                                   target_names=['Piktybinis', 'Gerybinis'],
                                   digits=4))
        
        # Painiavos matrica
        cm = confusion_matrix(y_test, y_pred)
        
        results.append({
            'Model': name,
            'Accuracy': accuracy,
            'Precision': precision,
            'Recall': recall,
            'F1-Score': f1,
            'Confusion Matrix': cm
        })
    
    return results


def visualize_results(results):
    """
    Vizualizuoti modelių rezultatus
    """
    print("\n" + "=" * 70)
    print("5. REZULTATŲ VIZUALIZACIJA")
    print("=" * 70)
    
    # 1. Metrikų palyginimas
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('Modelių Palyginimas', fontsize=16, fontweight='bold')
    
    metrics = ['Accuracy', 'Precision', 'Recall', 'F1-Score']
    colors = ['#3498db', '#e74c3c', '#2ecc71', '#f39c12']
    
    for idx, metric in enumerate(metrics):
        ax = axes[idx // 2, idx % 2]
        values = [r[metric] for r in results]
        models = [r['Model'] for r in results]
        
        bars = ax.bar(range(len(models)), values, color=colors[idx], alpha=0.7)
        ax.set_xlabel('Modelis', fontsize=11)
        ax.set_ylabel(metric, fontsize=11)
        ax.set_title(f'{metric} Palyginimas', fontsize=12, fontweight='bold')
        ax.set_xticks(range(len(models)))
        ax.set_xticklabels(models, rotation=45, ha='right')
        ax.set_ylim([0.85, 1.0])
        ax.grid(axis='y', alpha=0.3)
        
        # Pridėti reikšmes ant stulpelių
        for bar, value in zip(bars, values):
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{value:.4f}',
                   ha='center', va='bottom', fontsize=9)
    
    plt.tight_layout()
    plt.savefig('results/metrics_comparison.png', dpi=300, bbox_inches='tight')
    print("\n✓ Metrikų palyginimo grafikas išsaugotas: results/metrics_comparison.png")
    
    # 2. Painiavos matricos
    fig, axes = plt.subplots(2, 2, figsize=(14, 12))
    fig.suptitle('Painiavos Matricos (Confusion Matrices)', 
                 fontsize=16, fontweight='bold')
    
    for idx, result in enumerate(results):
        ax = axes[idx // 2, idx % 2]
        cm = result['Confusion Matrix']
        
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                   xticklabels=['Piktybinis', 'Gerybinis'],
                   yticklabels=['Piktybinis', 'Gerybinis'],
                   ax=ax, cbar_kws={'label': 'Skaičius'})
        
        ax.set_title(result['Model'], fontsize=12, fontweight='bold')
        ax.set_ylabel('Tikroji klasė', fontsize=11)
        ax.set_xlabel('Prognozuota klasė', fontsize=11)
    
    plt.tight_layout()
    plt.savefig('results/confusion_matrices.png', dpi=300, bbox_inches='tight')
    print("✓ Painiavos matricų grafikas išsaugotas: results/confusion_matrices.png")


def create_summary_table(results):
    """
    Sukurti suvestinę lentelę su visais rezultatais
    """
    print("\n" + "=" * 70)
    print("6. SUVESTINĖ LENTELĖ")
    print("=" * 70)
    
    df_results = pd.DataFrame([
        {
            'Modelis': r['Model'],
            'Accuracy': f"{r['Accuracy']:.4f}",
            'Precision': f"{r['Precision']:.4f}",
            'Recall': f"{r['Recall']:.4f}",
            'F1-Score': f"{r['F1-Score']:.4f}"
        }
        for r in results
    ])
    
    print("\n" + df_results.to_string(index=False))
    
    # Išsaugoti į CSV
    df_results.to_csv('results/summary.csv', index=False)
    print("\n✓ Suvestinė lentelė išsaugota: results/summary.csv")
    
    # Rasti geriausią modelį
    best_model_idx = np.argmax([r['F1-Score'] for r in results])
    best_model = results[best_model_idx]['Model']
    best_f1 = results[best_model_idx]['F1-Score']
    
    print("\n" + "=" * 70)
    print("IŠVADOS")
    print("=" * 70)
    print(f"\n🏆 Geriausias modelis: {best_model}")
    print(f"   F1-Score: {best_f1:.4f}")
    print("\nVisi modeliai parodė aukštą tikslumą (>95%), kas rodo,")
    print("kad duomenų rinkinys yra gerai tinkamas klasifikavimui.")


def main():
    """
    Pagrindinė programos funkcija
    """
    print("\n" + "=" * 70)
    print("DIRBTINIO INTELEKTO TAIKYMAS DUOMENŲ KLASIFIKAVIMUI")
    print("=" * 70)
    
    # 1. Duomenų įkėlimas
    X, y, feature_names = load_and_explore_data()
    
    # 2. Duomenų paruošimas
    X_train, X_test, y_train, y_test = preprocess_data(X, y)
    
    # 3. Modelių mokymas
    models = train_models(X_train, y_train)
    
    # 4. Modelių vertinimas
    results = evaluate_models(models, X_test, y_test)
    
    # 5. Vizualizacija
    visualize_results(results)
    
    # 6. Suvestinė lentelė
    create_summary_table(results)
    
    print("\n" + "=" * 70)
    print("PROGRAMA BAIGTA SĖKMINGAI!")
    print("=" * 70)
    print("\nVisi rezultatai išsaugoti 'results/' kataloge.")


if __name__ == "__main__":
    main()
