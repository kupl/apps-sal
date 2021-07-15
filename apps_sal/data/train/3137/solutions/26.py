from math import ceil,floor
def round_it(n):
    return ceil(n) if len(str(n).split('.')[0])<len(str(n).split('.')[1]) else floor(n) if len(str(n).split('.')[0])>len(str(n).split('.')[1]) else round(n)
