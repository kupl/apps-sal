import re
from math import gcd

def para_to_rect(eqn1, eqn2):
    eqn1, eqn2 = [re.sub(r'\bt', '1t', e) for e in [eqn1, eqn2]]
    (a,b), (c,d) = ([[int(x.replace(' ', '')) for x in re.findall('-?\d+|[-+] \d+', e)] for e in [eqn1, eqn2]])
    x = c*b - a*d
    g = gcd(gcd(c, a), x)
    if c < 0:
        g = -g
    c, a, x = c//g, a//g, x//g
    return re.sub(r'\b1([xy])', r'\1', f'{c}x {"+-"[a > 0]} {abs(a)}y = {x}')
