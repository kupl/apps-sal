two = "%&B8"
some = f"abdegopq069DOPQR{two}"

def countzero(string):
    return sum(2 if c in two else 1 for c in string.replace("()", "0") if c in some)
