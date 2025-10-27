# ⚡ Power Calculator

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE) 
Aplikácia na výpočet činného, jalového a zdanlivého výkonu pre 1-, 2- a 3-fázové zapojenia. Vhodná pre technikov, študentov aj domácich majstrov.

---

## ✨ Funkcie

- **Výpočet výkonov:**
  - Činný výkon (P) – užitočný výkon
  - Jalový výkon (Q) – induktívna/kapacitná zložka
  - Zdanlivý výkon (S) – celkový výkon

- **Podpora zapojení:**
  - 1-fázové (230 V)
  - 2-fázové medzifázové (L1–L2, 400 V)
  - 3-fázové (400 V)

- **Automatická kontrola vstupov:**
  - Napätie mimo rozsahu zvýrazní červeným pozadím
  - Pri neštandardnom vstupe sa automaticky nastaví typická hodnota (napr. 230 V alebo 400 V)

- **Prednastavené hodnoty pre rýchle testovanie**

- **Moderný vzhľad s vlastnými štýlmi (`ttk.Style`)**

- **Klávesové skratky:**
  - Ctrl+N – nový výpočet
  - Ctrl+Q – ukončenie aplikácie
  - F1 – okno O programe
  - ESC – zatvorenie okna O programe

- **Okno O programe:**
  - Vysvetlenie účinníka (cos φ)
  - Typické hodnoty pre rôzne typy záťaží

---

## 🧮 Výpočtová logika

Výpočty sa prispôsobujú podľa počtu fáz a vstupných hodnôt:

- **Zdanlivý výkon (S):**
  - 1 fáza: \( S = U \cdot I \)
  - 2 fázy: \( S = U \cdot I \)
  - 3 fázy: \( S = \sqrt{3} \cdot U \cdot I \)

- **Činný výkon (P):** \( P = S \cdot \cos\phi \)

- **Jalový výkon (Q):** \( Q = S \cdot \sin\phi \), kde \( \sin\phi = \sqrt{1 - \cos^2\phi} \)

- **Automatické korekcie napätia:**
  - 1 fáza: ak napätie ≥ 301 V → nastaví sa na 230 V
  - 2/3 fázy: ak napätie ≤ 300 V → nastaví sa na 400 V
  - Vstupné pole sa zvýrazní, ak je hodnota mimo typického rozsahu

---

## ⚡ Použitie

1. Zadaj prúd (A), napätie (V/ph) a účinník (cos φ)
2. Vyber počet fáz (1, 2 alebo 3)
3. Klikni na „Vypočítať výkon“ alebo stlač Ctrl+N
4. Výsledky sa zobrazia v spodnej časti okna:
   ```
   Active power (P):      xxx.xx W
   Apparent power (S):    xxx.xx VA
   Reactive power (Q):    xxx.xx VAr
   ```

---

## 🖼️ Ukážka

[![Ukážka aplikácie Power calculator](images/power.jpg)]

---

## 🚀 Spustenie

### 1. Požiadavky
- Python 3.8+
- Knižnice: `tkinter` (súčasť štandardnej knižnice)

### 2. Spustenie aplikácie

**Anglická verzia:**
```bash
python Power_calculator.py
```

**Slovenská verzia:**
```bash
python Power_calculator_sk.py
```

---

## 📄 Licencia

Tento projekt je licencovaný pod MIT License.  
© 2025 Igor Vitovský

---





