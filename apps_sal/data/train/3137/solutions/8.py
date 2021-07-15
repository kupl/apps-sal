import math
def round_it(a):
    b = list(map(len, str(a).split('.')))
    return  (math.ceil(a), int(a), round(a))[(b[0]>=b[1]) + (b[0]==b[1])]
