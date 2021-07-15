def decompose(n):
    # your code
    from fractions import Fraction
    f = Fraction(n)
    ret = []
    
    if 0 == f:
        return ret
    

    while not (f.numerator == 1 or f.denominator == 1):
        x = int(1/f) + 1
        ff = Fraction(1,x)
        ret.append(str(ff))
        f -= ff
    else:
        ret.append(str(f))
    
    return ret
