import pandas as pd


def nth_smallest(arr, pos):
    arr_series = pd.Series(arr)
    return arr_series.sort_values(ascending=True).reset_index(drop=True)[pos - 1]
