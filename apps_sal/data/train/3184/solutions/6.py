def total_bill(s):
    n,r=divmod(s.count('r'),5)
    return 8*n+2*r
