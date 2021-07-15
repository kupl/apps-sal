def vampire_test(x, y):
    return (str(x*y).count('1') == ((str(x).count('1')) + (str(y).count('1')))) & ((x > 0) | (y>0))
