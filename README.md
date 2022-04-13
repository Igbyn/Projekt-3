# Engeto projekt 3
Třetí projekt na python akademii.

## Popis projektu
Tento projekt získává data z voleb 2017.

## Instalace knihoven
Knihovny, které jsou použity jsou v souboru `requirements.txt` 

## Spuštění projektu
Pro spuštění souboru `elections-scraper.py` je zapotřebí napsat do příkazového řadku 2 argumenty.
```
py elections-craper.py <odkaz> <nazev souboru>
```
Následovně se informaci do souboru s příponnou `.csv`

## Ukázka projektu
Výsledky pro okres Domažlice:
1. argument: 'https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=4&xnumnuts=3201'
2. argument: 'hlasovani_domazlice'

Spuštění:
```
py elections-craper.py 'https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=4&xnumnuts=3201' 'hlasovani_domazlice'
```
Průběh stahování:
```
Stahuji z URL: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=4&xnumnuts=3201
Ukladam do souboru: hlasovani_domazlice.csv
Ukoncuji program
```