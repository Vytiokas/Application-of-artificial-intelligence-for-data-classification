# 🤖 Dirbtinio Intelekto Taikymas Duomenų Klasifikavimui

## 📖 Kas tai?
Šis projektas parodo, kaip kompiuteris gali išmokti atpažinti ligas! Naudojame 4 skirtingus "kompiuterio smegenius" (algoritmus), kad išmoktume atskirti sveikus audinius nuo sergančių.

## 🎯 Rezultatai
- **98.6% tikslumas** - iš 100 atvejų tik 1-2 klaidos!
- **4 algoritmai** išbandyti ir palyginti
- **Gražūs grafikai** ir vizualizacijos

## ⚡ Greitas startas (3 žingsniai)

### 1. Įdiegti bibliotekas
```bash
pip install -r requirements.txt
```

### 2. Paleisti programą
```bash
python src/main.py
```

### 3. Žiūrėti rezultatus
Rezultatai bus `results/` kataloge ir ekrane!

## 📁 Projekto struktūra

```
📂 Projektas/
├── 📄 README.md                    ← PRADĖK ČIA!
├── 📄 PAPRASTAS_PAAIŠKINIMAS.md    ← Paaiškinimas 15-mečiui
├── 📄 QUICK_START.md               ← Greitas startas
├── 📄 requirements.txt             ← Reikalingos bibliotekos
│
├── 📂 src/                         ← PROGRAMOS KODAS
│   ├── 🐍 main.py                  ← Pagrindinė programa
│   ├── 🐍 advanced_analysis.py     ← Išplėstinė analizė
│   └── 🐍 test_models.py           ← Eksperimentai
│
├── 📂 docs/                        ← DOKUMENTACIJA
│   ├── 📖 INSTRUKCIJOS.md          ← Detalios instrukcijos
│   ├── 📖 DOKUMENTACIJA.md         ← Išsami dokumentacija
│   └── 📖 PREZENTACIJA.md          ← Prezentacijos medžiaga
│
├── 📂 examples/                    ← PAVYZDŽIAI
│   └── 🐍 notebook_example.py      ← Jupyter Notebook versija
│
└── 📂 results/                     ← REZULTATAI (sukuriami automatiškai)
    ├── 📊 metrics_comparison.png   ← Algoritmų palyginimas
    ├── 🔢 confusion_matrices.png   ← Klaidų matricos
    └── 📋 summary.csv              ← Suvestinė lentelė
```

## 🧠 Algoritmai ir rezultatai

| Algoritmas | Tikslumas | Kaip veikia? |
|------------|-----------|--------------|
| 🧮 **Logistic Regression** | **98.6%** | Matematiniai skaičiavimai |
| 🌳 **Decision Tree** | 93.6% | Klausimų medis |
| 🌲 **Random Forest** | 96.6% | Daug medžių kartu |
| 🎯 **SVM** | **98.6%** | Ieško geriausios linijos |

## 📊 Duomenų rinkinys
- **Šaltinis:** Breast Cancer Wisconsin (UCI ML Repository)
- **Dydis:** 569 ląstelių pavyzdžiai
- **Požymiai:** 30 ląstelių savybių (dydis, forma, tekstūra)
- **Tikslas:** Atskirti geruosius navikus nuo piktybinių

## 🎓 Kam skirta?
- **Studentams** - mokytis mašininio mokymosi
- **Dėstytojams** - demonstracijoms ir užduotims
- **Programuotojams** - praktiniam AI taikymui
- **Visiems** - suprasti, kaip AI veikia medicinoje

## 🔍 Ką rasite?

### Programos:
- **src/main.py** - pagrindinė programa (PRADĖKITE ČIA!)
- **src/advanced_analysis.py** - išplėstinė analizė su ROC kreivėmis
- **src/test_models.py** - eksperimentai su parametrais

### Dokumentacija:
- **PAPRASTAS_PAAIŠKINIMAS.md** - paaiškinimas 15-mečiui 👶
- **QUICK_START.md** - greitas startas (3 žingsniai) ⚡
- **docs/INSTRUKCIJOS.md** - detalios instrukcijos 📋
- **docs/DOKUMENTACIJA.md** - išsami dokumentacija 📚

### Pavyzdžiai:
- **examples/notebook_example.py** - Jupyter Notebook versija

## 🚀 Paleidimo būdai

### Pradedantiesiems:
```bash
# 1. Įdiegti
pip install -r requirements.txt

# 2. Paleisti
python src/main.py

# 3. Žiūrėti results/ kataloge
```

### Pažengusiems:
```bash
# Išplėstinė analizė
python src/advanced_analysis.py

# Eksperimentai
python src/test_models.py
```

### Jupyter Notebook:
```bash
# Įdiegti Jupyter
pip install jupyter

# Paleisti
jupyter notebook

# Nukopijuoti kodą iš examples/notebook_example.py
```

## 📈 Kas bus sukurta?

Po paleidimo `results/` kataloge rasite:
- 📊 **metrics_comparison.png** - algoritmų palyginimo grafikai
- 🔢 **confusion_matrices.png** - klaidų matricos
- 📋 **summary.csv** - suvestinė lentelė
- ⭐ **feature_importance.png** - svarbiausi požymiai
- 📉 **roc_curves.png** - ROC kreivės

## 🛠️ Techniniai reikalavimai

### Programinė įranga:
- **Python 3.8+** (testuota su 3.13)
- **pip** (paketų tvarkyklė)

### Bibliotekos (automatiškai įdiegiamos):
- **numpy** - skaičiavimai
- **pandas** - duomenų tvarkymas
- **scikit-learn** - mašininis mokymasis
- **matplotlib** - grafikai
- **seaborn** - gražesni grafikai

### Sistemos reikalavimai:
- **RAM:** 2GB+ (rekomenduojama)
- **Vietos:** 100MB
- **Laikas:** 10-30 sekundžių paleidimui

## ❓ Dažni klausimai

### "Ar veiks mano kompiuteryje?"
Taip! Veikia Windows, Mac, Linux su Python 3.8+

### "Ar reikia programavimo žinių?"
Ne! Tiesiog paleiskite `python src/main.py`

### "Ar galiu keisti kodą?"
Žinoma! Kodas atviras ir gerai komentuotas

### "Kur gauti pagalbos?"
1. Skaitykite **PAPRASTAS_PAAIŠKINIMAS.md**
2. Žiūrėkite **QUICK_START.md**
3. Tikrinkite **docs/INSTRUKCIJOS.md**

## 🎯 Mokymosi kelias

### 1. Pradedantysis (5 min)
- Perskaitykite **PAPRASTAS_PAAIŠKINIMAS.md**
- Paleiskite `python src/main.py`
- Žiūrėkite grafikus

### 2. Pažengęs (30 min)
- Skaitykite **docs/DOKUMENTACIJA.md**
- Paleiskite `python src/advanced_analysis.py`
- Eksperimentuokite su parametrais

### 3. Ekspertas (2+ val)
- Keiskite kodą
- Naudokite savo duomenis
- Kurkite naujus algoritmus

## 🏆 Projekto privalumai

### ✅ Pilnai funkcionalus
- Veikia iš karto po įdiegimo
- Nėra klaidų ar trūkstamų failų

### ✅ Gerai dokumentuotas
- 8 dokumentacijos failai
- Komentarai kode
- Pavyzdžiai ir instrukcijos

### ✅ Lengvai pritaikomas
- Galite naudoti savo duomenis
- Keisti parametrus
- Pridėti naujų algoritmų

### ✅ Edukacinė vertė
- Mokymosi medžiaga
- Praktiniai pavyzdžiai
- Realūs rezultatai

## 📞 Palaikymas

### Problemos?
1. Tikrinkite Python versiją: `python --version`
2. Įdiekite bibliotekas: `pip install -r requirements.txt`
3. Skaitykite **docs/INSTRUKCIJOS.md**

### Klausimai?
- Skaitykite dokumentaciją `docs/` kataloge
- Žiūrėkite pavyzdžius `examples/` kataloge
- Eksperimentuokite su `src/test_models.py`

## 📜 Licencija

MIT License - laisvai naudokite, keiskite, dalinkitės!

## 🙏 Padėkos

- **Scikit-learn** komandai už puikią biblioteką
- **UCI ML Repository** už duomenų rinkinius
- **Python** bendruomenei už įrankius

---

## 🎉 Pradėkite dabar!

```bash
# Greičiausias būdas:
pip install -r requirements.txt && python src/main.py
```

**Sėkmės mokantis AI!** 🚀