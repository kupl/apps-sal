from fractions import gcd
import re


INSERTER = re.compile(r'(?<!\d)(?=[xyt])')
FINDER   = re.compile(r'-?\d+')


def lcm(a,b):    return a*b//gcd(a,b)
def simplify(s): return INSERTER.sub('1', s.replace(' ',''))


def para_to_rect(*equations):
    coefs = [ list(map(int, FINDER.findall(eq))) for eq in map(simplify, equations) ]
    l     = lcm(coefs[0][1],coefs[1][1])
    x,tx,cx, y,ty,cy = ( v*l//c[1] for c in coefs for v in c )
    y, absY, c = -y, abs(y), cx-cy
    
    return "{}x {} {}y = {}".format(x if x!=1 else '',
                                    '-' if y<0 else '+',
                                    absY if absY!=1 else '',
                                    c)
