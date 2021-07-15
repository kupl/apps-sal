def round_it(n):
    from math import floor,ceil
    f=[len(i) for i in str(n).split('.')]
    return round(n) if f[0]==f[1] else ceil(n) if f[0]<f[1] else floor(n)
