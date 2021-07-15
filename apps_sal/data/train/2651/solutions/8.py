def prod2sum(a,b,c,d):
    hi = sorted([abs(a*c+b*d), abs(a*d-b*c)])
    hello = sorted([abs(a*c-b*d), abs(a*d+b*c)])
    if hi == hello:
        return [hi]
    else:
        return sorted([hi, hello])
