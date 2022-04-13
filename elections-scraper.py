import requests
from bs4 import BeautifulSoup
import csv
import sys

try:
    link = sys.argv[1]
except IndexError:
    print("Vlozte odkaz a nazev souboru .csv")
    exit()

try:
    nazev = sys.argv[2]
except IndexError:
    print("Vlozte nazev souboru .csv")
    exit()

r = requests.get(link)
soup = BeautifulSoup(r.text, "html.parser")

def get_links() -> list:
    print(f"Stahuji z URL: {link}")
    rows = [["Kod obce", "Jmeno obce", "Volici v seznamu", "Vydane obalky", "Platne hlasy", "Kandidujici strany"]]
    for div in soup.find_all("div", {"class":"t3"}):
        for td in div.find_all("td", {"class":"cislo"}):
            rows.append(get_info(f"https://volby.cz/pls/ps2017nss/{td.find('a')['href']}"))
    return rows

def get_info(LINK) -> list:
    ro = requests.get(LINK)
    soupo = BeautifulSoup(ro.text, "html.parser")
    kod = soupo.find("main").find("a")["href"][30:36]
    h3s = soupo.find_all("h3")
    h3 = h3s[2]
    obec = ""
    for cast in h3.text.split()[1:]:
        obec = obec + cast + " "
    obec = obec[:-1]
    volici = soupo.find("td", {"headers":"sa2"}).text
    obalky = soupo.find("td", {"headers":"sa3"}).text
    hlasy = soupo.find("td", {"headers":"sa6"}).text
    strany = soupo.find("div", {"class":"t2_470"}).find_next("div", {"class":"t2_470"}).find_all("tr")[-1].find("td").text
    return [kod, obec, volici, obalky, hlasy, strany]

def vytvoreni_souboru():
    with open(f"{nazev}.csv", mode="w", encoding="utf-8", newline="") as f:
        fw = csv.writer(f)
        fw.writerows(get_links())
    print(f"Ukladam do souboru: {nazev}.csv")

vytvoreni_souboru()
print("Ukoncuji program")