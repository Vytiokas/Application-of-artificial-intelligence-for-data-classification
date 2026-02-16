# Dirbtinio Intelekto Taikymas Duomenų Klasifikavimui
## Projekto Prezentacija

---

## 📋 Projekto Apžvalga

**Tikslas:** Sukurti ir įvertinti mašininio mokymosi modelius medicininių duomenų klasifikavimui

**Duomenų rinkinys:** Breast Cancer Wisconsin
- 569 įrašai
- 30 požymių
- 2 klasės (gerybiniai / piktybiniai navikai)

**Įgyvendinti algoritmai:**
1. Logistic Regression
2. Decision Tree
3. Random Forest
4. Support Vector Machine (SVM)

---

## 📊 Duomenų Analizė

### Klasių Pasiskirstymas
- **Gerybiniai navikai:** 357 (62.7%)
- **Piktybiniai navikai:** 212 (37.3%)
- **Trūkstamos reikšmės:** 0
- **Duomenų kokybė:** Puiki

### Pagrindiniai Požymiai
- Geometriniai: spindulys, perimetras, plotas
- Tekstūriniai: tekstūra, lygumas
- Formos: kompaktiškumas, įgaubumas, simetrija

---

## 🔧 Metodologija

### 1. Duomenų Paruošimas
```
Duomenų rinkinys (569)
        ↓
Padalijimas (80/20)
        ↓
Mokymas: 455 | Testavimas: 114
        ↓
Standartizavimas (Z-score)
```

### 2. Modelių Mokymas
- Visi modeliai mokomi su tais pačiais duomenimis
- Naudojamas random_state=42 atkuriamumui
- Optimizuoti pagrindiniai parametrai

### 3. Vertinimas
**Metrikos:**
- Accuracy (bendras tikslumas)
- Precision (tikslumas teigiamoms prognozėms)
- Recall (atšaukimas)
- F1-Score (harmoninis vidurkis)

---

## 📈 Rezultatai

### Pagrindinės Metrikos

| Modelis | Accuracy | Precision | Recall | F1-Score |
|---------|----------|-----------|--------|----------|
| **Logistic Regression** | **98.25%** | **98.61%** | **98.61%** | **98.61%** |
| Decision Tree | 92.11% | 95.65% | 91.67% | 93.62% |
| Random Forest | 95.61% | 95.89% | 97.22% | 96.55% |
| **Support Vector Machine** | **98.25%** | **98.61%** | **98.61%** | **98.61%** |

### Geriausias Modelis
🏆 **Logistic Regression ir SVM** (F1-Score: 98.61%)

---

## 🔍 Išplėstinė Analizė

### Kryžminis Validavimas (5-Fold)
- **Logistic Regression:** 98.48% (±0.50%)
- **SVM:** 97.91% (±1.15%)
- **Random Forest:** 96.52% (±1.83%)
- **Decision Tree:** 93.49% (±1.56%)

### ROC AUC Rezultatai
- **Logistic Regression:** 0.9954
- **SVM:** 0.9950
- **Random Forest:** 0.9939
- **Decision Tree:** 0.9163

### Top 5 Svarbiausi Požymiai
1. Blogiausias plotas (worst area) - 13.94%
2. Blogiausias įgaubumas (worst concave points) - 13.22%
3. Vidutinis įgaubumas (mean concave points) - 10.70%
4. Blogiausias spindulys (worst radius) - 8.28%
5. Blogiausias perimetras (worst perimeter) - 8.08%

---

## 💡 Išvados

### Pagrindinės Išvados

1. **Puikūs rezultatai visų modelių**
   - Visi modeliai pasiekė >92% tikslumą
   - Duomenų rinkinys puikiai tinka klasifikavimui

2. **Geriausias modelis: Logistic Regression / SVM**
   - Aukščiausias F1-Score (98.61%)
   - Stabilūs rezultatai kryžminiame validavime
   - Mažiausiai klaidų

3. **Decision Tree atsiliko**
   - Žemiausias tikslumas (92.11%)
   - Didžiausias standartinis nuokrypis
   - Linkęs į persitreniravimą

4. **Požymių svarba**
   - Geometriniai požymiai (plotas, spindulys) svarbiausi
   - "Blogiausios" reikšmės informatyviausios
   - Tekstūriniai požymiai mažiau svarbūs

---

## 🎯 Praktinės Rekomendacijos

### Gamybai (Production)
✅ **Rekomenduojama:** SVM arba Random Forest
- Aukštas tikslumas
- Gera generalizacija
- Atsparus persitreniravimui

### Interpretacijai
✅ **Rekomenduojama:** Logistic Regression arba Decision Tree
- Lengvai interpretuojami sprendimai
- Svarbu medicininėse aplikacijose
- Galima paaiškinti pacientams

### Tolesni Žingsniai
1. **Hiperparametrų optimizavimas**
   - Grid Search / Random Search
   - Bayesian Optimization

2. **Ansamblio metodai**
   - Voting Classifier
   - Stacking

3. **Požymių inžinerija**
   - Naujų požymių kūrimas
   - Požymių selekcija

4. **Išorinis validavimas**
   - Nauji duomenys iš kitų ligoninių
   - Realaus pasaulio testavimas

---

## 📁 Projekto Struktūra

```
project/
├── main.py                    # Pagrindinė programa
├── advanced_analysis.py       # Išplėstinė analizė
├── test_models.py            # Papildomi testai
├── notebook_example.py       # Jupyter Notebook versija
├── requirements.txt          # Bibliotekos
├── README.md                 # Projekto aprašymas
├── DOKUMENTACIJA.md          # Išsami dokumentacija
├── INSTRUKCIJOS.md           # Naudojimo instrukcijos
├── PREZENTACIJA.md           # Ši prezentacija
└── results/                  # Rezultatai
    ├── metrics_comparison.png
    ├── confusion_matrices.png
    ├── feature_importance.png
    ├── roc_curves.png
    └── summary.csv
```

---

## 🛠️ Naudotos Technologijos

**Programavimo kalba:**
- Python 3.8+

**Bibliotekos:**
- **numpy** - skaičiavimams
- **pandas** - duomenų tvarkymui
- **scikit-learn** - mašininio mokymosi algoritmai
- **matplotlib** - vizualizacijai
- **seaborn** - pažangesnei vizualizacijai

**Aplinka:**
- Jupyter Notebook (pasirinktinai)
- Git (versijų kontrolei)

---

## 📚 Literatūra

1. **Scikit-learn dokumentacija**
   - https://scikit-learn.org/

2. **UCI Machine Learning Repository**
   - https://archive.ics.uci.edu/ml/

3. **Breast Cancer Wisconsin Dataset**
   - Original paper: W.N. Street, W.H. Wolberg and O.L. Mangasarian (1993)

4. **Knygos:**
   - "Hands-On Machine Learning" - Aurélien Géron
   - "Pattern Recognition and Machine Learning" - Christopher Bishop
   - "The Elements of Statistical Learning" - Hastie, Tibshirani, Friedman

---

## ❓ Klausimai ir Atsakymai

### Kodėl pasirinktas šis duomenų rinkinys?
- Gerai žinomas ir patikimas
- Medicininė svarba
- Puiki duomenų kokybė
- Tinkamas demonstracijai

### Kodėl naudojamas standartizavimas?
- SVM ir Logistic Regression jautrūs skalei
- Pagerina konvergenciją
- Standartinė praktika

### Kaip interpretuoti F1-Score?
- Harmoninis Precision ir Recall vidurkis
- Gerai veikia su nesubalansuotais duomenimis
- 1.0 = tobulas klasifikatorius

### Ar galima naudoti kitiems duomenims?
- Taip! Kodas lengvai pritaikomas
- Reikia pakeisti tik duomenų įkėlimo dalį
- Visi algoritmai universalūs

---

## 🎓 Projekto Vertė

### Demonstruoja:
✅ Pilną mašininio mokymosi workflow  
✅ Keturių algoritmų palyginimą  
✅ Tinkamą duomenų paruošimą  
✅ Išsamų modelių vertinimą  
✅ Profesionalią vizualizaciją  
✅ Praktines rekomendacijas  

### Įgūdžiai:
- Python programavimas
- Duomenų analizė
- Mašininis mokymasis
- Vizualizacija
- Dokumentavimas

---

## 📞 Kontaktai

**Projektas sukurtas kaip universiteto užduotis**

Dėl klausimų ar pasiūlymų:
- Peržiūrėkite DOKUMENTACIJA.md
- Skaitykite INSTRUKCIJOS.md
- Bandykite test_models.py

---

## 🙏 Padėkos

- **Scikit-learn** komandai už puikią biblioteką
- **UCI ML Repository** už duomenų rinkinius
- **Python** bendruomenei už įrankius
- Dėstytojui už užduotį ir palaikymą

---

# Ačiū už dėmesį! 🎉

**Projektas baigtas sėkmingai!**

Visi rezultatai prieinami `results/` kataloge.
