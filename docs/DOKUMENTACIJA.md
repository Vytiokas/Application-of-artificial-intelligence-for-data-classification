# Projekto Dokumentacija

## Turinys
1. [Įvadas](#įvadas)
2. [Duomenų rinkinys](#duomenų-rinkinys)
3. [Metodologija](#metodologija)
4. [Algoritmai](#algoritmai)
5. [Rezultatai](#rezultatai)
6. [Išvados](#išvados)

## Įvadas

Šis projektas demonstruoja mašininio mokymosi algoritmų taikymą medicininių duomenų klasifikavimui. Tikslas - sukurti modelį, kuris gali tiksliai klasifikuoti navikus kaip geruosius arba piktybinius pagal jų charakteristikas.

## Duomenų rinkinys

### Breast Cancer Wisconsin Dataset

**Šaltinis:** UCI Machine Learning Repository (prieinamas per scikit-learn)

**Aprašymas:**
- Duomenys surinkti iš skaitmeninių krūties masės smulkiųjų adatų aspiracijos (FNA) vaizdų
- Kiekvienas įrašas aprašo ląstelių branduolių charakteristikas

**Statistika:**
- Įrašų skaičius: 569
- Požymių skaičius: 30
- Klasės:
  - Gerybiniai navikai (1): 357 (62.7%)
  - Piktybiniai navikai (0): 212 (37.3%)

**Požymiai:**
Kiekvienam branduoliui apskaičiuojami 10 požymių:
1. Spindulys (radius)
2. Tekstūra (texture)
3. Perimetras (perimeter)
4. Plotas (area)
5. Lygumas (smoothness)
6. Kompaktiškumas (compactness)
7. Įgaubumas (concavity)
8. Įgaubtų taškų skaičius (concave points)
9. Simetrija (symmetry)
10. Fraktalinis matmuo (fractal dimension)

Kiekvienam požymiui apskaičiuojama:
- Vidurkis (mean)
- Standartinė paklaida (standard error)
- "Blogiausias" arba didžiausias (mean of the three largest values)

**Duomenų kokybė:**
- Nėra trūkstamų reikšmių
- Visi požymiai yra skaitiniai
- Duomenys yra gerai subalansuoti

## Metodologija

### 1. Duomenų paruošimas

#### Padalijimas
- Mokymo rinkinys: 80% (455 įrašai)
- Testavimo rinkinys: 20% (114 įrašų)
- Naudojamas stratifikuotas padalijimas (stratify=y)

#### Standartizavimas
Taikomas Z-score standartizavimas:
```
z = (x - μ) / σ
```
Kur:
- x - pradinė reikšmė
- μ - vidurkis
- σ - standartinis nuokrypis

**Priežastis:** Skirtingi požymiai turi labai skirtingas skales (pvz., plotas vs. simetrija), todėl standartizavimas būtinas algoritmams, kurie jautrūs skalei (SVM, Logistic Regression).

### 2. Modelių mokymas

Visi modeliai mokomi naudojant tą patį mokymo rinkinį su standartizuotais duomenimis.

### 3. Vertinimas

#### Metrikos

**Accuracy (Tikslumas):**
```
Accuracy = (TP + TN) / (TP + TN + FP + FN)
```

**Precision (Tikslumas):**
```
Precision = TP / (TP + FP)
```

**Recall (Atšaukimas):**
```
Recall = TP / (TP + FN)
```

**F1-Score:**
```
F1 = 2 × (Precision × Recall) / (Precision + Recall)
```

Kur:
- TP = True Positives (teisingai prognozuoti teigiami)
- TN = True Negatives (teisingai prognozuoti neigiami)
- FP = False Positives (klaidingai prognozuoti teigiami)
- FN = False Negatives (klaidingai prognozuoti neigiami)

## Algoritmai

### 1. Logistic Regression (Logistinė Regresija)

**Principas:**
- Naudoja logistinę funkciją tikimybei modeliuoti
- Tiesinis klasifikatorius
- Greitai mokosi ir prognozuoja

**Parametrai:**
- max_iter=10000 (maksimalus iteracijų skaičius)
- random_state=42 (atkuriamumas)

**Privalumai:**
- Paprastas ir interpretuojamas
- Greitas mokymas
- Gerai veikia su tiesiškai atskiriamais duomenimis

**Trūkumai:**
- Negali modeliuoti sudėtingų netiesinių ryšių
- Jautrus išskirtims

### 2. Decision Tree (Sprendimų Medis)

**Principas:**
- Rekursyviai dalija duomenis pagal požymius
- Kuria medžio struktūrą su sprendimų taisyklėmis
- Netiesinis klasifikatorius

**Parametrai:**
- max_depth=5 (maksimalus medžio gylis)
- random_state=42

**Privalumai:**
- Lengvai interpretuojamas
- Gali modeliuoti netiesinius ryšius
- Nereikalauja duomenų standartizavimo

**Trūkumai:**
- Linkęs į persitreniravimą (overfitting)
- Nestabilus (maži duomenų pokyčiai gali keisti medį)

### 3. Random Forest (Atsitiktinis Miškas)

**Principas:**
- Ansamblio metodas - sujungia daug sprendimų medžių
- Kiekvienas medis mokomas su atsitiktine duomenų ir požymių imtimi
- Galutinė prognozė - balsavimas

**Parametrai:**
- n_estimators=100 (medžių skaičius)
- random_state=42

**Privalumai:**
- Labai tikslus
- Atsparus persitreniravimui
- Gali įvertinti požymių svarbą
- Gerai veikia su dideliais duomenų rinkiniais

**Trūkumai:**
- Lėtesnis nei pavieniai medžiai
- Mažiau interpretuojamas
- Reikalauja daugiau atminties

### 4. Support Vector Machine (Atraminių Vektorių Mašina)

**Principas:**
- Ieško optimalios hiperplokštumos, kuri atskiria klases
- Naudoja branduolio funkciją (kernel) netiesiniams ryšiams
- Maksimizuoja atstumą tarp klasių (margin)

**Parametrai:**
- kernel='rbf' (Radial Basis Function - Gauso branduolys)
- random_state=42

**Privalumai:**
- Efektyvus didelių dimensijų erdvėse
- Atsparus persitreniravimui
- Gerai veikia su aiškiai atskiriamomis klasėmis

**Trūkumai:**
- Lėtas su dideliais duomenų rinkiniais
- Jautrus parametrų pasirinkimui
- Sunku interpretuoti

## Rezultatai

### Pagrindiniai rezultatai

| Modelis | Accuracy | Precision | Recall | F1-Score |
|---------|----------|-----------|--------|----------|
| Logistic Regression | ~0.97 | ~0.98 | ~0.98 | ~0.98 |
| Decision Tree | ~0.94 | ~0.94 | ~0.97 | ~0.95 |
| Random Forest | ~0.97 | ~0.98 | ~0.98 | ~0.98 |
| SVM | ~0.98 | ~0.99 | ~0.98 | ~0.98 |

*Pastaba: Tikslūs rezultatai gali šiek tiek skirtis dėl atsitiktinumo*

### Painiavos matricos

Painiavos matricos rodo, kaip modeliai klasifikuoja kiekvieną klasę:
- Diagonalė rodo teisingas prognozes
- Kiti elementai rodo klaidas

### ROC kreivės

ROC (Receiver Operating Characteristic) kreivės rodo modelio gebėjimą atskirti klases:
- AUC (Area Under Curve) > 0.99 visiems modeliams
- Rodo puikų klasifikavimo gebėjimą

### Požymių svarba

Random Forest analizė rodo svarbiausius požymius:
1. Blogiausias perimetras (worst perimeter)
2. Blogiausias spindulys (worst radius)
3. Vidutinis įgaubumas (mean concave points)
4. Blogiausias plotas (worst area)
5. Vidutinis perimetras (mean perimeter)

## Išvados

### Pagrindinės išvados

1. **Visi modeliai pasiekė aukštą tikslumą (>94%)**
   - Rodo, kad duomenų rinkinys yra gerai tinkamas klasifikavimui
   - Požymiai yra informatyvūs ir gerai atskiria klases

2. **Geriausias modelis: SVM arba Random Forest**
   - Pasiekė aukščiausią F1-Score (~0.98)
   - Mažiausiai klaidų klasifikavime

3. **Decision Tree šiek tiek atsiliko**
   - Tikriausiai dėl persitreniravimo tendencijos
   - Galima pagerinti optimizuojant max_depth parametrą

4. **Požymių svarba**
   - Geometriniai požymiai (perimetras, spindulys, plotas) yra svarbiausi
   - "Blogiausios" reikšmės (worst) yra informatyviausios

### Praktinės rekomendacijos

1. **Gamybai:** Rekomenduojama naudoti Random Forest arba SVM
   - Aukštas tikslumas
   - Gera generalizacija

2. **Interpretacijai:** Logistic Regression arba Decision Tree
   - Lengviau paaiškinti sprendimus
   - Svarbu medicininėse aplikacijose

3. **Tolesni žingsniai:**
   - Hiperparametrų optimizavimas (Grid Search, Random Search)
   - Ansamblio metodų taikymas (Voting, Stacking)
   - Daugiau požymių inžinerijos
   - Išorinio validavimo rinkinys

### Projekto vertė

Šis projektas demonstruoja:
- Pilną mašininio mokymosi workflow
- Keturių skirtingų algoritmų palyginimą
- Tinkamą duomenų paruošimą ir vertinimą
- Rezultatų vizualizavimą ir interpretaciją
- Praktines rekomendacijas

## Literatūra ir šaltiniai

1. Scikit-learn dokumentacija: https://scikit-learn.org/
2. UCI Machine Learning Repository: https://archive.ics.uci.edu/ml/
3. Breast Cancer Wisconsin Dataset: https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+(Diagnostic)
4. "Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow" - Aurélien Géron
5. "Pattern Recognition and Machine Learning" - Christopher Bishop
