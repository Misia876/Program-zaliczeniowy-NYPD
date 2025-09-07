import numpy as np
import pandas as pd
import csv
import os
import requests
import argparse

def test_populacja(populacja_wojewodztw_sorted, ludnosc_polska):
    suma_populacji = populacja_wojewodztw_sorted['Populacja'].sum()
    roznica_populacji = suma_populacji - ludnosc_polska

    return roznica_populacji


def test_pozary(pozar_na_wojewodztwo_sorted):
    suma_pozarow = pozar_na_wojewodztwo_sorted.loc[:, ['Mały (P/M)', 'Średni (P/Ś)', 'Duży (P/D)', 'Bardzo duży (P/BD)']].sum(axis=1)
    pozary_lacznie = pozar_na_wojewodztwo_sorted['RAZEM Pożar (P)']
    roznica_pozarow = suma_pozarow.sum() - pozary_lacznie.sum()

    return roznica_pozarow