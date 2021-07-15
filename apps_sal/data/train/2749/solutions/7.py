def solve(a):
    c = sum((b>a)-(b<a) + 1j*(b-a) for a,b in zip(a, a[1:]))
    return 'R'*(len(a)-abs(c.real)!= 1) + 'DA'[c.real>0 if c.real else c.imag<0]
