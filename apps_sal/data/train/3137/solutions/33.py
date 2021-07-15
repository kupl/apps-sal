from math import floor
from math import ceil
def round_it(n):
    a = list(map(len,  str(n).split('.')))
    if a[0] == a[1]:
        return round(n)
    elif a[0] > a[1]:
        return floor(n)
    elif a[0] < a[1]:
        return ceil(n)
