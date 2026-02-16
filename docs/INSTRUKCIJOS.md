# Naudojimo Instrukcijos

## Sistemos reikalavimai

- Python 3.8 arba naujesnė versija
- pip (Python paketų tvarkyklė)
- 100 MB laisvos vietos diske

## Įdiegimas

### 1. Parsisiųsti projektą

```bash
# Jei naudojate Git
git clone <repository-url>
cd <project-folder>

# Arba tiesiog išpakuokite ZIP failą
```

### 2. Sukurti virtualią aplinką (rekomenduojama)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Įdiegti reikalingas bibliotekas

```bash
pip install -r requirements.txt
```

Tai įdiegs:
- numpy (skaičiavimams)
- pandas (duomenų tvarkymui)
- scikit-learn (mašininio mokymosi algoritmai)
- matplotlib (vizualizacijai)
- seaborn (pažangesnei vizualizacijai)

## Paleidimas

### Pagrindinė programa

```bash
python main.py
```

**Kas vyksta:**
1. Įkeliami duomenys
2. Atliekamas duomenų paruošimas
3. Mokomi 4 modeliai
4. Vertinami rezultatai
5. Kuriamos vizualizacijos
6. Spausdinamos išvados

**Trukmė:** ~10-30 sekundžių (priklauso nuo kompiuterio)

**Rezultatai:**
- Konsolėje: Išsami informacija apie kiekvieną etapą
- `results/metrics_comparison.png` - Metrikų palyginimas
- `results/confusion_matrices.png` - Painiavos matricos
- `results/summary.csv` - Suvestinė lentelė

### Išplėstinė analizė

```bash
python advanced_analysis.py
```

**Papildomos funkcijos:**
- 5-fold kryžminis validavimas
- Požymių svarbos analizė
- ROC kreivės

**Rezultatai:**
- `results/feature_importance.png` - Požymių svarba
- `results/roc_curves.png` - ROC kreivės

## Projekto struktūra

```
project/
│
├── main.py                  # Pagrindinė programa
├── advanced_analysis.py     # Išplėstinė analizė
├── requirements.txt         # Reikalingos bibliotekos
├── README.md               # Projekto aprašymas
├── DOKUMENTACIJA.md        # Išsami dokumentacija
├── INSTRUKCIJOS.md         # Šis failas
├── .gitignore             # Git ignoruojami failai
│
└── results/               # Rezultatų katalogas (sukuriamas automatiškai)
    ├── metrics_comparison.png
    ├── confusion_matrices.png
    ├── feature_importance.png
    ├── roc_curves.png
    └── summary.csv
```

## Dažniausiai pasitaikančios problemos

### 1. ModuleNotFoundError

**Problema:** `ModuleNotFoundError: No module named 'sklearn'`

**Sprendimas:**
```bash
pip install scikit-learn
```

### 2. Matplotlib neveikia

**Problema:** Grafikai nesukuriami arba nerodomi

**Sprendimas:**
```bash
# Windows
pip install matplotlib --upgrade

# Linux (gali reikėti papildomų paketų)
sudo apt-get install python3-tk
```

### 3. Lėtas veikimas

**Problema:** Programa vykdoma labai ilgai

**Sprendimas:**
- Patikrinkite, ar turite pakankamai RAM (rekomenduojama >2GB)
- Sumažinkite Random Forest n_estimators parametrą (pvz., nuo 100 iki 50)

### 4. Encoding klaidos

**Problema:** Lietuviški simboliai rodomi neteisingai

**Sprendimas:**
- Naudokite UTF-8 palaikantį terminalą
- Windows: `chcp 65001` prieš paleidžiant programą

## Modifikavimas

### Keisti duomenų rinkinį

`main.py` faile pakeiskite `load_and_explore_data()` funkciją:

```python
def load_and_explore_data():
    # Vietoj load_breast_cancer() naudokite savo duomenis
    X = pd.read_csv('jusu_duomenys.csv')
    y = X['target_column']
    X = X.drop('target_column', axis=1)
    return X, y, X.columns
```

### Pridėti naują modelį

`main.py` faile `train_models()` funkcijoje:

```python
models = {
    'Logistic Regression': LogisticRegression(...),
    'Decision Tree': DecisionTreeClassifier(...),
    'Random Forest': RandomForestClassifier(...),
    'SVM': SVC(...),
    'Naujas Modelis': JusuModelis(...)  # Pridėkite čia
}
```

### Keisti parametrus

Redaguokite modelių parametrus `train_models()` funkcijoje:

```python
'Random Forest': RandomForestClassifier(
    n_estimators=200,      # Pakeiskite iš 100
    max_depth=10,          # Pridėkite naują parametrą
    random_state=42
)
```

## Papildoma informacija

### Kaip skaityti rezultatus

**Accuracy (Tikslumas):**
- 0.95 = 95% visų prognozių yra teisingos
- Aukštesnis = geriau

**Precision (Tikslumas):**
- Iš visų teigiamų prognozių, kiek yra tikrai teigiamos
- Svarbu, kai False Positive yra brangu

**Recall (Atšaukimas):**
- Iš visų tikrų teigiamų, kiek modelis surado
- Svarbu, kai False Negative yra brangu

**F1-Score:**
- Harmoninis Precision ir Recall vidurkis
- Geras bendras rodiklis

**Confusion Matrix:**
```
                Prognozuota
              Neg    Pos
Tikroji  Neg  TN     FP
         Pos  FN     TP
```

### Kur gauti pagalbos

1. Scikit-learn dokumentacija: https://scikit-learn.org/stable/
2. Stack Overflow: https://stackoverflow.com/questions/tagged/scikit-learn
3. Python dokumentacija: https://docs.python.org/3/

## Licencija

Šis projektas yra sukurtas mokymo tikslais ir gali būti laisvai naudojamas ir modifikuojamas.

## Autoriai

Projektas sukurtas kaip universiteto užduotis "Dirbtinio intelekto taikymas duomenų klasifikavimui".
