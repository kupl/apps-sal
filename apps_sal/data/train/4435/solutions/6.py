from re import findall;
from functools import reduce
gcd=lambda a,b: gcd(b,a%b) if b else a;
has_subpattern=lambda s: len(s)>1 and reduce(gcd, (len(e[0]+e[1]) for e in findall(r"(.)(\1*)", "".join(sorted(s)))))>1
