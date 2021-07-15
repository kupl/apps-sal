from math import floor, ceil 

def round_it(n):
    string = str(n)
    point_ix = string.index('.')
    if len(string[:point_ix]) == len(string[point_ix+1:]):
        return round(n)
    if len(string[:point_ix]) > len(string[point_ix+1:]):
        return floor(n)
    return ceil(n)
