import pandas as pd


def get_average(marks):
    s = pd.Series(marks)
    return int(s.mean())
