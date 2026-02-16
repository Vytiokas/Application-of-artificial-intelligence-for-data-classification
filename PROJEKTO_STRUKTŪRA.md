# 📁 Projekto Struktūra

## 🗂️ Failų organizacija

```
🤖 Dirbtinio-Intelekto-Projektas/
│
├── 📄 README.md                    ← 🎯 PRADĖK ČIA! Projekto aprašymas
├── 📄 PAPRASTAS_PAAIŠKINIMAS.md    ← 👶 Paaiškinimas 15-mečiui
├── 📄 QUICK_START.md               ← ⚡ Greitas startas (3 žingsniai)
├── 📄 CHECKLIST.md                 ← ✅ Tikrinimo sąrašas
├── 📄 requirements.txt             ← 📦 Reikalingos bibliotekos
├── 📄 LICENSE.txt                  ← 📜 Licencija
├── 📄 .gitignore                   ← 🚫 Git ignoruojami failai
│
├── 📂 src/                         ← 🐍 PROGRAMOS KODAS
│   ├── 🐍 main.py                  ← ⭐ Pagrindinė programa (PALEISK!)
│   ├── 🐍 advanced_analysis.py     ← 🔬 Išplėstinė analizė
│   └── 🐍 test_models.py           ← 🧪 Eksperimentai ir testai
│
├── 📂 docs/                        ← 📚 DOKUMENTACIJA
│   ├── 📖 INSTRUKCIJOS.md          ← 📋 Detalios naudojimo instrukcijos
│   ├── 📖 DOKUMENTACIJA.md         ← 📚 Išsami dokumentacija (500+ eilučių)
│   ├── 📖 PREZENTACIJA.md          ← 🎤 Prezentacijos medžiaga
│   ├── 📖 PROJECT_SUMMARY.md       ← 📊 Projekto santrauka
│   ├── 📖 RESOURCES.md             ← 🔗 Naudingos nuorodos
│   └── 📄 STRUCTURE.txt            ← 🗂️ Sena struktūros informacija
│
├── 📂 examples/                    ← 📓 PAVYZDŽIAI
│   └── 🐍 notebook_example.py      ← 📓 Jupyter Notebook versija
│
└── 📂 results/                     ← 📊 REZULTATAI (sukuriami automatiškai)
    ├── 📊 metrics_comparison.png   ← Algoritmų palyginimo grafikai
    ├── 🔢 confusion_matrices.png   ← Klaidų matricos (4 modeliai)
    ├── ⭐ feature_importance.png    ← Požymių svarbos analizė
    ├── 📉 roc_curves.png           ← ROC kreivės
    └── 📋 summary.csv              ← Suvestinė lentelė
```

## 🎯 Failų paskirtis

### 📄 Pagrindiniai failai (šakniniame kataloge)

| Failas | Paskirtis | Kam skirta |
|--------|-----------|------------|
| **README.md** | Projekto aprašymas | Visiems - pradžia |
| **PAPRASTAS_PAAIŠKINIMAS.md** | Paprastas paaiškinimas | 15-mečiams ir pradedantiesiems |
| **QUICK_START.md** | Greitas startas | Norintiems greitai paleisti |
| **CHECKLIST.md** | Tikrinimo sąrašas | Užduočių tikrinimui |
| **requirements.txt** | Python bibliotekos | Automatiniam įdiegimui |

### 🐍 Programos kodas (src/)

| Failas | Eilučių | Paskirtis | Paleidimas |
|--------|---------|-----------|------------|
| **main.py** | ~300 | Pagrindinė programa | `python src/main.py` |
| **advanced_analysis.py** | ~200 | Išplėstinė analizė | `python src/advanced_analysis.py` |
| **test_models.py** | ~200 | Eksperimentai | `python src/test_models.py` |

### 📚 Dokumentacija (docs/)

| Failas | Eilučių | Paskirtis | Kam skirta |
|--------|---------|-----------|------------|
| **INSTRUKCIJOS.md** | ~300 | Detalios instrukcijos | Norintiems suprasti viską |
| **DOKUMENTACIJA.md** | ~500 | Išsami dokumentacija | Akademiniam darbui |
| **PREZENTACIJA.md** | ~400 | Prezentacijos medžiaga | Pristatymams |
| **PROJECT_SUMMARY.md** | ~200 | Projekto santrauka | Greitam peržiūrėjimui |
| **RESOURCES.md** | ~300 | Naudingos nuorodos | Tolimesniam mokymuisi |

### 📓 Pavyzdžiai (examples/)

| Failas | Paskirtis | Naudojimas |
|--------|-----------|------------|
| **notebook_example.py** | Jupyter Notebook versija | Nukopijuoti į Jupyter |

### 📊 Rezultatai (results/)

| Failas | Formatas | Turinys |
|--------|----------|---------|
| **metrics_comparison.png** | PNG | 4 metrikų palyginimo grafikai |
| **confusion_matrices.png** | PNG | 4 algoritmų klaidų matricos |
| **feature_importance.png** | PNG | Požymių svarbos analizė |
| **roc_curves.png** | PNG | ROC kreivės su AUC |
| **summary.csv** | CSV | Suvestinė lentelė su rezultatais |

## 🚀 Naudojimo schema

### 1. Pradedantysis (5 min)
```
README.md → PAPRASTAS_PAAIŠKINIMAS.md → python src/main.py
```

### 2. Normalus vartotojas (15 min)
```
README.md → QUICK_START.md → python src/main.py → results/
```

### 3. Pažengęs (30 min)
```
docs/INSTRUKCIJOS.md → python src/main.py → python src/advanced_analysis.py
```

### 4. Ekspertas (1+ val)
```
docs/DOKUMENTACIJA.md → visų programų paleidimas → kodo modifikavimas
```

## 📈 Projekto statistika

### Failų skaičius:
- **Python failai:** 4
- **Dokumentacijos failai:** 9
- **Konfigūracijos failai:** 3
- **Rezultatų failai:** 5 (sukuriami automatiškai)
- **Iš viso:** 21 failas

### Kodo statistika:
- **Kodo eilučių:** ~700
- **Dokumentacijos eilučių:** ~2000+
- **Komentarų:** Išsamūs visur
- **Funkcijų:** 15+

### Katalogų struktūra:
- **src/** - Kodas (3 failai)
- **docs/** - Dokumentacija (6 failai)
- **examples/** - Pavyzdžiai (1 failas)
- **results/** - Rezultatai (5 failai, sukuriami automatiškai)

## 🎯 Kokį failą skaityti?

### Jei esate...

**👶 Pradedantysis (15 metų):**
1. `PAPRASTAS_PAAIŠKINIMAS.md` - suprasite, kas vyksta
2. `README.md` - pamatysite bendrą vaizdą
3. `QUICK_START.md` - paleisti programą

**🎓 Studentas (užduotis):**
1. `README.md` - projekto aprašymas
2. `docs/DOKUMENTACIJA.md` - išsami informacija
3. `CHECKLIST.md` - patikrinti, ar viskas padaryta

**👨‍🏫 Dėstytojas (vertinimas):**
1. `docs/PROJECT_SUMMARY.md` - greitas projekto apžvalga
2. `docs/PREZENTACIJA.md` - prezentacijos medžiaga
3. `results/summary.csv` - rezultatų lentelė

**💻 Programuotojas (kodas):**
1. `src/main.py` - pagrindinė programa
2. `docs/INSTRUKCIJOS.md` - kaip modifikuoti
3. `src/test_models.py` - eksperimentai

**🔬 Tyrinėtojas (metodologija):**
1. `docs/DOKUMENTACIJA.md` - išsami metodologija
2. `src/advanced_analysis.py` - išplėstinė analizė
3. `docs/RESOURCES.md` - papildomi ištekliai

## 🛠️ Kaip pridėti naują failą?

### Programos kodas:
```
src/naujas_failas.py
```

### Dokumentacija:
```
docs/NAUJAS_DOKUMENTAS.md
```

### Pavyzdžiai:
```
examples/naujas_pavyzdys.py
```

### Rezultatai:
```
results/ (sukuriami automatiškai)
```

## 🔄 Failų priklausomybės

### main.py priklauso nuo:
- `requirements.txt` (bibliotekos)
- `results/` katalogo (rezultatams)

### Dokumentacija priklauso nuo:
- Programos veikimo
- Rezultatų failų
- Vienas nuo kito (nuorodos)

### Pavyzdžiai priklauso nuo:
- `requirements.txt`
- Pagrindinės programos logikos

## 📋 Failų tikrinimo sąrašas

### Prieš pateikimą patikrinkite:
- [ ] Visi Python failai veikia be klaidų
- [ ] Sukuriami rezultatų failai
- [ ] Dokumentacija atitinka kodą
- [ ] Nuorodos tarp failų veikia
- [ ] requirements.txt pilnas

### Kokybės kriterijai:
- [ ] Kodas komentuotas
- [ ] Dokumentacija išsami
- [ ] Failai logiškai suskirstyti
- [ ] Struktūra aiški ir suprantama

## 🎉 Išvada

Projektas yra gerai organizuotas su aiškia struktūra:
- **Kodas** atskirtas nuo **dokumentacijos**
- **Pavyzdžiai** atskirti nuo **pagrindinių failų**
- **Rezultatai** sukuriami automatiškai
- **Dokumentacija** pritaikyta skirtingiems vartotojams

**Projektas paruoštas naudojimui ir pateikimui!** 🏆