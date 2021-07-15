from math import gcd

def para_to_rect(eqn1, eqn2):
    a, b = eqn1.split('= ')[1].split('t ')
    c, d = eqn2.split('= ')[1].split('t ')
    if a in ("", "-"): a += '1'
    if c in ("", "-"): c += '1'
    a, b, c, d = map(eval, (a, b, c, d))
    x = gcd(a, c)
    e, f = c//x, -a//x
    if e < 0: e, f = -e, -f
    return f"{e if e>1 else ''}x {'+-'[f<0]} {abs(f) if abs(f)>1 else ''}y = {e*b + f*d}"
