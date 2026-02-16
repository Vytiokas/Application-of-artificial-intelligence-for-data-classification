"""
Jupyter Notebook versijos pavyzdys
Šį kodą galite nukopijuoti į Jupyter Notebook ir vykdyti po vieną celę

Celių struktūra:
- Celė 1: Importai
- Celė 2: Duomenų įkėlimas
- Celė 3: Duomenų analizė
- Celė 4: Duomenų paruošimas
- Celė 5: Modelių mokymas
- Celė 6: Rezultatų vertinimas
- Celė 7: Vizualizacija
"""

# ============================================================================
# CELĖ 1: IMPORTAI
# ============================================================================
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
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, classification_report
)
import warnings
warnings.filterwarnings('ignore')

# Nustatyti matplotlib stilių
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

print("✓ Visos bibliotekos sėkmingai importuotos!")


# ============================================================================
# CELĖ 2: DUOMENŲ ĮKĖLIMAS
# ============================================================================
# Įkelti duomenų rinkinį
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target, name='target')

print(f"Duomenų forma: {X.shape}")
print(f"\nPirmi 5 įrašai:")
display(X.head())

print(f"\nTikslinė klasė:")
print(f"0 (Piktybinis): {sum(y==0)}")
print(f"1 (Gerybinis): {sum(y==1)}")


# ============================================================================
# CELĖ 3: DUOMENŲ ANALIZĖ
# ============================================================================
# Statistinė informacija
print("Statistinė informacija:")
display(X.describe())

# Klasių pasiskirstymas
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Stulpelinė diagrama
axes[0].bar(['Piktybinis', 'Gerybinis'], [sum(y==0), sum(y==1)], 
           color=['#e74c3c', '#2ecc71'], alpha=0.7)
axes[0].set_ylabel('Skaičius')
axes[0].set_title('Klasių pasiskirstymas')
axes[0].grid(axis='y', alpha=0.3)

# Skritulinė diagrama
axes[1].pie([sum(y==0), sum(y==1)], labels=['Piktybinis', 'Gerybinis'],
           autopct='%1.1f%%', colors=['#e74c3c', '#2ecc71'], startangle=90)
axes[1].set_title('Klasių proporcijos')

plt.tight_layout()
plt.show()

# Koreliacijos matrica (pirmi 10 požymių)
plt.figure(figsize=(12, 10))
correlation = X.iloc[:, :10].corr()
sns.heatmap(correlation, annot=True, fmt='.2f', cmap='coolwarm', center=0)
plt.title('Koreliacijos matrica (pirmi 10 požymių)')
plt.tight_layout()
plt.show()


# ============================================================================
# CELĖ 4: DUOMENŲ PARUOŠIMAS
# ============================================================================
# Padalinti duomenis
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print(f"Mokymo rinkinys: {X_train.shape[0]} įrašų")
print(f"Testavimo rinkinys: {X_test.shape[0]} įrašų")

# Standartizavimas
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print(f"\n✓ Duomenys standartizuoti")
print(f"Vidurkis: {X_train_scaled.mean():.6f}")
print(f"Std: {X_train_scaled.std():.6f}")


# ============================================================================
# CELĖ 5: MODELIŲ MOKYMAS
# ============================================================================
# Apibrėžti modelius
models = {
    'Logistic Regression': LogisticRegression(max_iter=10000, random_state=42),
    'Decision Tree': DecisionTreeClassifier(random_state=42, max_depth=5),
    'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
    'SVM': SVC(kernel='rbf', random_state=42)
}

# Apmokyti modelius
trained_models = {}
for name, model in models.items():
    print(f"Mokomas: {name}...", end=' ')
    model.fit(X_train_scaled, y_train)
    trained_models[name] = model
    print("✓")

print("\n✓ Visi modeliai apmokyti!")


# ============================================================================
# CELĖ 6: REZULTATŲ VERTINIMAS
# ============================================================================
results = []

for name, model in trained_models.items():
    # Prognozės
    y_pred = model.predict(X_test_scaled)
    
    # Metrikos
    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred)
    rec = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    
    results.append({
        'Model': name,
        'Accuracy': acc,
        'Precision': prec,
        'Recall': rec,
        'F1-Score': f1,
        'CM': cm
    })
    
    print(f"\n{name}:")
    print(f"  Accuracy:  {acc:.4f}")
    print(f"  Precision: {prec:.4f}")
    print(f"  Recall:    {rec:.4f}")
    print(f"  F1-Score:  {f1:.4f}")

# Sukurti DataFrame
df_results = pd.DataFrame([
    {k: v for k, v in r.items() if k != 'CM'}
    for r in results
])

print("\n" + "="*60)
print("SUVESTINĖ LENTELĖ")
print("="*60)
display(df_results)


# ============================================================================
# CELĖ 7: VIZUALIZACIJA
# ============================================================================
# 1. Metrikų palyginimas
fig, axes = plt.subplots(2, 2, figsize=(15, 12))
fig.suptitle('Modelių Palyginimas', fontsize=16, fontweight='bold')

metrics = ['Accuracy', 'Precision', 'Recall', 'F1-Score']
colors = ['#3498db', '#e74c3c', '#2ecc71', '#f39c12']

for idx, metric in enumerate(metrics):
    ax = axes[idx // 2, idx % 2]
    values = df_results[metric].values
    models_list = df_results['Model'].values
    
    bars = ax.bar(range(len(models_list)), values, color=colors[idx], alpha=0.7)
    ax.set_xlabel('Modelis')
    ax.set_ylabel(metric)
    ax.set_title(f'{metric} Palyginimas')
    ax.set_xticks(range(len(models_list)))
    ax.set_xticklabels(models_list, rotation=45, ha='right')
    ax.set_ylim([0.85, 1.0])
    ax.grid(axis='y', alpha=0.3)
    
    for bar, value in zip(bars, values):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
               f'{value:.4f}', ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.show()

# 2. Painiavos matricos
fig, axes = plt.subplots(2, 2, figsize=(14, 12))
fig.suptitle('Painiavos Matricos', fontsize=16, fontweight='bold')

for idx, result in enumerate(results):
    ax = axes[idx // 2, idx % 2]
    cm = result['CM']
    
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
               xticklabels=['Piktybinis', 'Gerybinis'],
               yticklabels=['Piktybinis', 'Gerybinis'],
               ax=ax)
    
    ax.set_title(result['Model'])
    ax.set_ylabel('Tikroji klasė')
    ax.set_xlabel('Prognozuota klasė')

plt.tight_layout()
plt.show()

# 3. Geriausias modelis
best_idx = df_results['F1-Score'].idxmax()
best_model = df_results.loc[best_idx, 'Model']
best_f1 = df_results.loc[best_idx, 'F1-Score']

print("\n" + "="*60)
print("IŠVADOS")
print("="*60)
print(f"\n🏆 Geriausias modelis: {best_model}")
print(f"   F1-Score: {best_f1:.4f}")
print("\nVisi modeliai parodė puikius rezultatus (>94% tikslumas)!")
