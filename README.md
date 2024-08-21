# Testare Automată DemoBlaze

Acest proiect utilizează **Selenium WebDriver** și **Python** pentru a realiza teste automate asupra aplicației web [DemoBlaze](https://www.demoblaze.com/). Suplimentar, folosește și framework-ul **Behave** pentru implementarea testării bazate pe BDD (Behavior-Driven Development).

## Structura Proiectului

- **`features/`**: Fișierele `.feature` care definesc scenariile de testare în stil BDD.
- **`page/`**: Conține clase pentru interacțiunea cu diverse pagini web, utilizând modelul Page Object.
- **`steps/`**: Include definițiile pașilor (steps) pentru fiecare scenariu BDD.
- **`browser.py`**: Gestionează inițializarea WebDriver-ului pentru diferite browsere.
- **`behave.ini`**: Fișier de configurare pentru framework-ul Behave.
- **`environment.py`**: Configurația mediului de testare.

## Cerințe

- **Python 3.x**
- **Selenium WebDriver**
- **Behave**
- **Webdriver (ex. ChromeDriver)**

### Instalare și Setup

1. Clonează repository-ul:
    ```bash
    git clone https://github.com/poprobert0412/TestareAutomataDemoBlaze.git
    ```

2. Instalează dependențele:
    ```bash
    pip install -r requirements.txt
    ```

3. Descarcă și adaugă în `PATH` driver-ul browserului ales (de ex. **ChromeDriver**).

## Rularea Testelor

Pentru a rula testele folosind Behave:

```bash
behave
```

Raportul HTML generat va fi disponibil după rularea testelor.

## Structura Directorului

- **`features/`**: Conține fișiere `.feature` pentru diferite scenarii de testare.
- **`page/`**: Clase care descriu elementele și acțiunile paginilor web (Page Object Model).
- **`steps/`**: Definiții ale pașilor pentru scenariile descrise în `.feature`.
- **`report.html`** și **`behave-report.html`**: Rapoarte detaliate ale rulării testelor.

## Configurare Browsere

În fișierul `browser.py` poți configura browserul utilizat pentru testare (implicit este Chrome). Dacă vrei să folosești un alt browser, asigură-te că ai driverul necesar și editează codul în consecință.

## Contribuții

Orice contribuție este binevenită. Urmează acești pași:

1. Creează un fork.
2. Creează o ramură nouă (`git checkout -b feature-noua`).
3. Comite modificările (`git commit -m 'Adaugă o nouă funcționalitate'`).
4. Trimite modificările (`git push origin feature-noua`).
5. Creează un Pull Request.

## Licență

Acest proiect este licențiat sub licența MIT.
