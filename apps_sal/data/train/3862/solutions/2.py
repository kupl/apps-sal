from string import ascii_lowercase as aLow

TABLE = str.maketrans(aLow, aLow[::-1])

def mirror(code, alpha=None):
    table = TABLE if alpha is None else str.maketrans(alpha, alpha[::-1]) 
    return code.lower().translate(table)
