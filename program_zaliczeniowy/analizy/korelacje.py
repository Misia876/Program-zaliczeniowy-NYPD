import numpy as np
import pandas as pd

def macierz_korelacji(dane):
    return dane.corr()

def konkretna_korelacja(macierz_korelacji, var1, var2):
    return macierz_korelacji.loc[var1, var2]