import numpy as np
import pandas as pd


def statystyki(dane):
    return { 
        "średnia": dane.mean(),
        "mediana": dane.median(),
        "odchylenie standardowe": dane.std()
    }