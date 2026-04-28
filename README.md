# Notatnik CLI

Prosta, szybka i bezpieczna aplikacja konsolowa do zarządzania notatkami tekstowymi napisana w Pythonie.

---

## Opis

**Notatnik CLI** to aplikacja dla osób, które preferują pracę w terminalu oraz chcą mieć pełną kontrolę nad swoimi danymi. Projekt skupia się na prostocie, bezpieczeństwie i czytelnej architekturze.

---

## Funkcjonalności

### Zarządzanie notatkami
- Dodawanie nowych notatek  
- Wyświetlanie listy notatek  
- Usuwanie notatek  

### Wyszukiwanie
- Wyszukiwanie po tytule  
- Wyszukiwanie po treści  

### Bezpieczeństwo
- Dostęp zabezpieczony hasłem  
- Hashowanie SHA-256  

### Logowanie
- Zapisywanie operacji do folderu `logs/`  
- Rejestrowanie dodania i usunięcia notatek  

### Trwałość danych
- Dane przechowywane w bazie SQLite  

---

## Struktura projektu
Notatnik_CLI/
├── data/              # Baza danych SQLite i plik hasła 
├── logs/              # Logi systemowe aplikacji 
├── src/               # Kod źródłowy programu 
│ ├── main.py          # Punkt wejścia (CLI) 
│ ├── notes_manager.py # Logika bazy danych i operacji 
│ └── utils.py         # Funkcje pomocnicze i bezpieczeństwo 
├── tests/             # Testy jednostkowe (pytest) 
├── .gitignore         # Pliki ignorowane przez Git 
├── requirements.txt   # Lista zależności 
└── README.md          # Dokumentacja projektu

---

## Instalacja i uruchomienie

git clone <url-twojego-repozytorium>  
cd Notatnik_CLI  

py -m pip install pytest  

python src/main.py list  

Przy pierwszym uruchomieniu zostaniesz poproszony o ustawienie hasła.

---

## Użycie

Dodanie notatki:  
python src/main.py add --title "Zakupy" --content "Mleko, chleb, masło" --cat "Dom"  

Lista notatek:  
python src/main.py list  

Wyszukiwanie:  
python src/main.py search "Mleko"  

Usuwanie:  
python src/main.py delete 1  

---

## Testy

pytest tests/

---

## Technologie

Python 3.x  
Argparse  
SQLite3  
Hashlib (SHA-256)  
Pytest  
