# ⚡ Greitas Pradžios Vadovas

## 🎯 3 Žingsniai iki Rezultatų

### 1️⃣ Įdiegti bibliotekas
```bash
pip install -r requirements.txt
```

### 2️⃣ Paleisti programą
```bash
python src/main.py
```

### 3️⃣ Peržiūrėti rezultatus
Rezultatai bus:
- **Ekrane** - skaičiai ir informacija
- **results/** kataloge - gražūs grafikai

---

## 📦 Kas yra projekte?

### 🐍 Programos (src/):
- **main.py** - Pagrindinė programa (PRADĖK ČIA!)
- **advanced_analysis.py** - Išplėstinė analizė
- **test_models.py** - Papildomi eksperimentai

### 📚 Dokumentacija (docs/):
- **INSTRUKCIJOS.md** - Detalios instrukcijos
- **DOKUMENTACIJA.md** - Išsami dokumentacija
- **PREZENTACIJA.md** - Prezentacijos medžiaga

### 📓 Pavyzdžiai (examples/):
- **notebook_example.py** - Jupyter Notebook versija

---

## 🎯 Kas bus padaryta?

1. ✅ Įkelti Breast Cancer duomenų rinkinį (569 įrašai)
2. ✅ Paruošti duomenis (padalijimas, standartizavimas)
3. ✅ Apmokyti 4 modelius:
   - Logistic Regression
   - Decision Tree
   - Random Forest
   - Support Vector Machine
4. ✅ Įvertinti rezultatus (Accuracy, Precision, Recall, F1)
5. ✅ Sukurti vizualizacijas (grafikai, matricos)
6. ✅ Pateikti išvadas

**Trukmė:** ~10-30 sekundžių

---

## 📊 Ko tikėtis?

### Konsolėje:
```
======================================================================
DIRBTINIO INTELEKTO TAIKYMAS DUOMENŲ KLASIFIKAVIMUI
======================================================================

1. DUOMENŲ ĮKĖLIMAS IR ANALIZĖ
   - Duomenų rinkinio dydis: 569 įrašų, 30 požymių
   - Klasių pasiskirstymas: 62.7% / 37.3%

2. DUOMENŲ PARUOŠIMAS
   - Mokymo rinkinys: 455 įrašų
   - Testavimo rinkinys: 114 įrašų

3. MODELIŲ MOKYMAS
   ✓ Logistic Regression apmokytas
   ✓ Decision Tree apmokytas
   ✓ Random Forest apmokytas
   ✓ SVM apmokytas

4. MODELIŲ VERTINIMAS
   Logistic Regression: Accuracy 98.25%, F1-Score 98.61%
   Decision Tree: Accuracy 92.11%, F1-Score 93.62%
   Random Forest: Accuracy 95.61%, F1-Score 96.55%
   SVM: Accuracy 98.25%, F1-Score 98.61%

5. REZULTATŲ VIZUALIZACIJA
   ✓ Grafikai išsaugoti results/ kataloge

6. IŠVADOS
   🏆 Geriausias modelis: Logistic Regression (F1: 98.61%)
```

### Failuose (results/):
- **metrics_comparison.png** - Metrikų palyginimo grafikai
- **confusion_matrices.png** - Painiavos matricos
- **summary.csv** - Suvestinė lentelė
- **feature_importance.png** - Požymių svarba (advanced_analysis.py)
- **roc_curves.png** - ROC kreivės (advanced_analysis.py)

---

## 🚀 Papildomi Paleidimo Būdai

### Išplėstinė analizė:
```bash
python src/advanced_analysis.py
```

### Eksperimentai:
```bash
python src/test_models.py
```

### Jupyter Notebook:
```bash
# 1. Įdiegti Jupyter
pip install jupyter

# 2. Paleisti
jupyter notebook

# 3. Sukurti naują notebook ir nukopijuoti kodą iš notebook_example.py
```

---

## ❗ Dažniausios Problemos

### Problema: "ModuleNotFoundError"
**Sprendimas:**
```bash
pip install numpy pandas scikit-learn matplotlib seaborn
```

### Problema: Grafikai nesukuriami
**Sprendimas:**
```bash
# Windows
pip install matplotlib --upgrade

# Linux
sudo apt-get install python3-tk
```

### Problema: Lietuviški simboliai rodomi neteisingai
**Sprendimas (Windows):**
```bash
chcp 65001
python main.py
```

---

## 📖 Tolimesni Žingsniai

### Noriu suprasti kodą:
1. Skaityk **DOKUMENTACIJA.md** - išsami informacija
2. Peržiūrėk **main.py** - kodas su komentarais
3. Bandyk **test_models.py** - eksperimentuok

### Noriu modifikuoti:
1. Pakeisk parametrus `train_models()` funkcijoje
2. Pridėk naują modelį į `models` dictionary
3. Naudok savo duomenis `load_and_explore_data()` funkcijoje

### Noriu pristatyti:
1. Naudok **PREZENTACIJA.md** kaip šabloną
2. Rodyti grafikus iš `results/` katalogo
3. Paaiškink rezultatus iš `summary.csv`

---

## 🎓 Mokymosi Ištekliai

### Pradedantiesiems:
- [Python Tutorial](https://docs.python.org/3/tutorial/)
- [Pandas Tutorial](https://pandas.pydata.org/docs/getting_started/intro_tutorials/)
- [Scikit-learn Tutorial](https://scikit-learn.org/stable/tutorial/index.html)

### Pažengusiems:
- [Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course)
- [Kaggle Learn](https://www.kaggle.com/learn)
- [Fast.ai](https://www.fast.ai/)

### Knygos:
- "Hands-On Machine Learning" - Aurélien Géron
- "Python Data Science Handbook" - Jake VanderPlas

---

## ✅ Checklist Užduočiai

- [ ] Įdiegtos visos bibliotekos
- [ ] Paleista main.py programa
- [ ] Peržiūrėti rezultatai konsolėje
- [ ] Atidaryti grafikai iš results/
- [ ] Paleista advanced_analysis.py
- [ ] Perskaityta DOKUMENTACIJA.md
- [ ] Suprastos pagrindinės metrikos
- [ ] Paruošta prezentacija (jei reikia)
- [ ] Patikrintas kodas su komentarais
- [ ] Išbandyti test_models.py eksperimentai

---

## 💬 Patarimai

### ✨ Geriausia praktika:
1. **Pradėk nuo main.py** - tai pagrindinė programa
2. **Skaityk komentarus** - kodas gerai komentuotas
3. **Eksperimentuok** - keisk parametrus ir žiūrėk rezultatus
4. **Vizualizuok** - grafikai padeda suprasti
5. **Dokumentuok** - rašyk, ką darai ir kodėl

### 🎯 Užduočiai:
- Visi reikalavimai įgyvendinti ✅
- 4 algoritmai realizuoti ✅
- Visos metrikos apskaičiuotos ✅
- Vizualizacijos sukurtos ✅
- Kodas komentuotas ✅
- Dokumentacija parašyta ✅

### 🏆 Papildomi taškai:
- Išplėstinė analizė (kryžminis validavimas, ROC)
- Požymių svarbos analizė
- Parametrų optimizavimas
- Jupyter Notebook versija
- Išsami dokumentacija lietuvių kalba

---

## 🎉 Sėkmės!

Jei kyla klausimų:
1. Skaityk **INSTRUKCIJOS.md**
2. Peržiūrėk **DOKUMENTACIJA.md**
3. Bandyk **test_models.py**

**Projektas yra pilnai funkcionalus ir paruoštas naudojimui!**
