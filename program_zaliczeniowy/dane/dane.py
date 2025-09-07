import numpy as np
import pandas as pd
import requests

def dane():

    url = 'https://api.dane.gov.pl/resources/64719,1-zdarzenia-wg-rodzaju-i-wielkosci-w-rozbiciu-na-wojewodztwo-powiat-gmine/csv'

    response = requests.get(url)
    file_Path = 'pozar.csv'

    if response.status_code == 200:
        with open(file_Path, 'wb') as file:
            file.write(response.content)
        print('File downloaded successfully')
    else:
        print('Failed to download file')



    url = 'https://api.dane.gov.pl/resources/64402,wykaz-przedsiebiorcow-majacych-zezwolenia-na-handel-hurtowy-napojami-alkoholowymi-na-dzien-20250204/file'

    response = requests.get(url)
    file_Path = 'alkohol.csv'

    if response.status_code == 200:
        with open(file_Path, 'wb') as file:
            file.write(response.content)
        print('File downloaded successfully')
    else:
        print('Failed to download file')


    pozar = pd.read_csv('pozar.csv')

    alkohol = pd.read_csv('alkohol.csv')

    ludnosc = pd.read_csv('dane/ludnosc.csv',sep=';', encoding='utf-8', skiprows=3)

    ludnosc_polska = ludnosc.iloc[0, 4]

    alkohol_liczba_firm_na_wojewodztwo = alkohol['Województwo'].value_counts()
    alkohol_reset=alkohol_liczba_firm_na_wojewodztwo.reset_index()
    alkohol_sorted=alkohol_reset.sort_values('Województwo')

    populacja_wojewodztw = ludnosc.iloc[2:, [1, 4]]
    populacja_wojewodztw.columns = ['Województwo', 'Populacja']
    populacja_wojewodztw = populacja_wojewodztw.reset_index(drop=True)
    populacja_wojewodztw_sorted=populacja_wojewodztw.sort_values('Województwo')

    pozar_na_wojewodztwo = pozar.groupby('Województwo')[['RAZEM Pożar (P)', 'Mały (P/M)', 'Średni (P/Ś)', 'Duży (P/D)', 'Bardzo duży (P/BD)']].sum().reset_index()
    pozar_na_wojewodztwo_sorted=pozar_na_wojewodztwo.sort_values('Województwo')
    

    #moja korelacja: fałszywe alarmy a populacja
    pozar_alarmy = pozar.groupby('Województwo')['RAZEM Alarm fałszywy (AF)'].sum().reset_index()
    pozar_alarmy_sorted=pozar_alarmy.sort_values('Województwo')
    

    zlaczone_dict = {'populacja': populacja_wojewodztw_sorted['Populacja'], 'pozary': pozar_na_wojewodztwo_sorted['RAZEM Pożar (P)'], 'alkohol': alkohol_sorted['count'], 'pozar_alarmy': pozar_alarmy_sorted['RAZEM Alarm fałszywy (AF)']}
    zlaczone = pd.concat(zlaczone_dict, axis=1)
    
    return zlaczone, populacja_wojewodztw_sorted, ludnosc_polska, pozar_na_wojewodztwo_sorted

