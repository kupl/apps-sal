def integrate(coefficient, exponent):
    s = int(coefficient/(exponent+1))
    d = exponent+1
    return str(s)+'x'+'^'+str(d)
w = integrate(12,5)
print(w)
