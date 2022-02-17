
# KaRo ==> Dane Książki

Ten projekt pozwala zamienieć numer isbn Książki za pomocą danych znalezionych w serwisie https://karo.umk.pl/ na łatwą w edycji listę w języku python. 

## Użycie

Instalacja bibliotek:

```bash
  pip install bs4
  pip install requests
```

Następnie w pliku main.py na samym dole zmieniamy numer isbn na własny i uruchamiamy program:
```bash
  python3 main.py
```

# UWAGI
W ostatniej lini:
```py
  print(get_data(9788381181341, 'BN')) #lib = BN - Biblioteka Narodowa, UJ - Biblioteka jagielońska
```
W miejscu "BN" wpisujemy kod biblioteki z której pobieramy dane
W miejscu liczby "9788381181341" wpisujemy isbn
