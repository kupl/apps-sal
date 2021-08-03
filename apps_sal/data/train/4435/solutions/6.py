from re import findall
from functools import reduce
def gcd(a, b): return gcd(b, a % b) if b else a
def has_subpattern(s): return len(s) > 1 and reduce(gcd, (len(e[0] + e[1]) for e in findall(r"(.)(\1*)", "".join(sorted(s))))) > 1
