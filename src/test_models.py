"""
Papildomi testai ir eksperimentai
Šis failas leidžia išbandyti skirtingus parametrus ir palyginimus
"""

import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, f1_score
import warnings
warnings.filterwarnings('ignore')


def test_random_forest_parameters():
    """
    Testuoti skirtingus Random Forest parametrus
    """
    print("=" * 70)
    print("RANDOM FOREST PARAMETRŲ OPTIMIZAVIMAS")
    print("=" * 70)
    
    # Įkelti duomenis
    data = load_breast_cancer()
    X, y = data.data, data.target
    
    # Padalinti ir standartizuoti
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Parametrų tinklelis
    param_grid = {
        'n_estimators': [50, 100, 200],
        'max_depth': [3, 5, 7, None],
        'min_samples_split': [2, 5, 10]
    }
    
    print("\nIeškoma geriausių parametrų...")
    print(f"Testuojama kombinacijų: {len(param_grid['n_estimators']) * len(param_grid['max_depth']) * len(param_grid['min_samples_split'])}")
    
    # Grid Search
    rf = RandomForestClassifier(random_state=42)
    grid_search = GridSearchCV(
        rf, param_grid, cv=5, scoring='f1', n_jobs=-1, verbose=1
    )
    grid_search.fit(X_train_scaled, y_train)
    
    # Rezultatai
    print("\n" + "=" * 70)
    print("REZULTATAI")
    print("=" * 70)
    print(f"\nGeriausi parametrai:")
    for param, value in grid_search.best_params_.items():
        print(f"  {param}: {value}")
    
    print(f"\nGeriausias F1-Score (cross-validation): {grid_search.best_score_:.4f}")
    
    # Testuoti su testavimo rinkiniu
    best_model = grid_search.best_estimator_
    y_pred = best_model.predict(X_test_scaled)
    test_f1 = f1_score(y_test, y_pred)
    
    print(f"F1-Score su testavimo rinkiniu: {test_f1:.4f}")
    
    print("\nKlasifikacijos ataskaita:")
    print(classification_report(y_test, y_pred, 
                               target_names=['Piktybinis', 'Gerybinis']))
    
    return grid_search.best_params_, grid_search.best_score_


def compare_with_without_scaling():
    """
    Palyginti modelių veikimą su ir be standartizavimo
    """
    print("\n" + "=" * 70)
    print("STANDARTIZAVIMO ĮTAKA")
    print("=" * 70)
    
    # Įkelti duomenis
    data = load_breast_cancer()
    X, y = data.data, data.target
    
    # Padalinti
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    # Standartizuoti
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Testuoti Random Forest
    print("\nRandom Forest:")
    
    # Be standartizavimo
    rf_no_scale = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_no_scale.fit(X_train, y_train)
    y_pred_no_scale = rf_no_scale.predict(X_test)
    f1_no_scale = f1_score(y_test, y_pred_no_scale)
    
    # Su standartizavimu
    rf_scale = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_scale.fit(X_train_scaled, y_train)
    y_pred_scale = rf_scale.predict(X_test_scaled)
    f1_scale = f1_score(y_test, y_pred_scale)
    
    print(f"  Be standartizavimo: F1-Score = {f1_no_scale:.4f}")
    print(f"  Su standartizavimu: F1-Score = {f1_scale:.4f}")
    print(f"  Skirtumas: {abs(f1_scale - f1_no_scale):.4f}")
    
    if f1_scale > f1_no_scale:
        print("  ✓ Standartizavimas pagerino rezultatus")
    elif f1_scale < f1_no_scale:
        print("  ✗ Standartizavimas pablogino rezultatus")
    else:
        print("  = Standartizavimas neturėjo įtakos")


def test_different_train_sizes():
    """
    Testuoti, kaip mokymo rinkinio dydis įtakoja rezultatus
    """
    print("\n" + "=" * 70)
    print("MOKYMO RINKINIO DYDŽIO ĮTAKA")
    print("=" * 70)
    
    # Įkelti duomenis
    data = load_breast_cancer()
    X, y = data.data, data.target
    
    # Standartizuoti visus duomenis
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Testuoti skirtingus dydžius
    train_sizes = [0.5, 0.6, 0.7, 0.8, 0.9]
    
    print("\nRandom Forest rezultatai su skirtingais mokymo rinkinio dydžiais:")
    print("-" * 70)
    
    results = []
    for size in train_sizes:
        X_train, X_test, y_train, y_test = train_test_split(
            X_scaled, y, train_size=size, random_state=42, stratify=y
        )
        
        rf = RandomForestClassifier(n_estimators=100, random_state=42)
        rf.fit(X_train, y_train)
        y_pred = rf.predict(X_test)
        f1 = f1_score(y_test, y_pred)
        
        results.append({
            'Train Size': f"{size*100:.0f}%",
            'Train Samples': len(X_train),
            'Test Samples': len(X_test),
            'F1-Score': f1
        })
        
        print(f"  {size*100:.0f}% mokymo ({len(X_train)} įrašų): F1-Score = {f1:.4f}")
    
    # Rasti geriausią
    best_idx = np.argmax([r['F1-Score'] for r in results])
    best_size = results[best_idx]['Train Size']
    best_f1 = results[best_idx]['F1-Score']
    
    print(f"\n✓ Geriausias rezultatas su {best_size} mokymo duomenų: {best_f1:.4f}")


def main():
    """
    Paleisti visus testus
    """
    print("\n" + "=" * 70)
    print("PAPILDOMI TESTAI IR EKSPERIMENTAI")
    print("=" * 70)
    
    # 1. Parametrų optimizavimas
    best_params, best_score = test_random_forest_parameters()
    
    # 2. Standartizavimo įtaka
    compare_with_without_scaling()
    
    # 3. Mokymo rinkinio dydžio įtaka
    test_different_train_sizes()
    
    print("\n" + "=" * 70)
    print("VISI TESTAI BAIGTI!")
    print("=" * 70)
    
    print("\nPagrindinės išvados:")
    print("1. Parametrų optimizavimas gali pagerinti rezultatus")
    print("2. Random Forest mažai jautrus standartizavimui")
    print("3. Didesnis mokymo rinkinys paprastai duoda geresnius rezultatus")


if __name__ == "__main__":
    main()
