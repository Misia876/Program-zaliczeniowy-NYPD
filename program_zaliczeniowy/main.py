import numpy as np
import pandas as pd
import argparse


#ARGPARSE
parser = argparse.ArgumentParser(description='Zapis danych do pliku CSV')
parser.add_argument('nazwa_pliku', help='Nazwa pliku wyjściowego (bez .csv)')
parser.add_argument('--nadpisz', action='store_true', help='Nadpisz istniejący plik')
args = parser.parse_args()
sciezka = f"{args.nazwa_pliku}.csv"

#wywoływanie
from .analizy.statystyki import statystyki 
from .analizy.korelacje import macierz_korelacji, konkretna_korelacja
from .dane.dane import dane
from .testy.testy import test_populacja, test_pozary

def main():
    zlaczone, populacja_wojewodztw_sorted, ludnosc_polska, pozar_na_wojewodztwo_sorted = dane()
    #statystyki
    stat_popul = statystyki(zlaczone["populacja"])
    print("Statystyki dla populacji:")
    for nazwa, wartosc in stat_popul.items():
        print(f"{nazwa}: {wartosc}")

    stat_poz = statystyki(zlaczone["pozary"])
    print("Statystyki dla pożarów:")
    for nazwa, wartosc in stat_poz.items():
        print(f"{nazwa}: {wartosc}")

    stat_alko = statystyki(zlaczone["alkohol"])
    print("Statystyki dla alkoholu:")
    for nazwa, wartosc in stat_alko.items():
        print(f"{nazwa}: {wartosc}")

    #korelacje
    korelacje = macierz_korelacji(zlaczone)
    print(f"Macierz korelacji: {korelacje}")
    
    #populacja_pożary
    popul_poz = konkretna_korelacja(korelacje, 'populacja', 'pozary')
    print(f"Korelacja między liczbą ludności a ilością pożarów: {popul_poz}")

    #populacja_alkohol
    popul_alko = konkretna_korelacja(korelacje, 'populacja', 'alkohol')
    print(f"Korelacja między liczbą ludności a spożyciem alkoholu: {popul_alko}")

    #pożary_alkohol
    poz_alko = konkretna_korelacja(korelacje, 'pozary', 'alkohol')
    print(f"Korelacja między ilością pożarów a spożyciem alkoholu: {poz_alko}")

    #moja korelacja: pożary fałszywe alarmy_populacja
    #populacja_alkohol
    alarm_popul = konkretna_korelacja(korelacje, 'pozar_alarmy', 'populacja')
    print(f"Korelacja między ilością fałszywych alarmów pożarowych a liczbą ludnośc: {alarm_popul}")

    #niespójności
    roznica_populacji = test_populacja(populacja_wojewodztw_sorted, ludnosc_polska)
    print(f'Różnica między sumą populacji województw a populacją Polski: {roznica_populacji}')

    roznica_pozarow = test_pozary(pozar_na_wojewodztwo_sorted)
    print(f"Różnica między sumą pożarów różnej wielkości a łączną liczbą pożarów: {roznica_pozarow}")


if __name__ == "__main__":
    main()