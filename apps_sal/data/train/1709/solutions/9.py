import subprocess
from itertools import chain


def prime_factors(n):
    out = subprocess.run(['factor', str(n)], stdout=subprocess.PIPE)
    out = str(out).split(':')[1].split('\\n')[0].split()
    return [int(s) for s in out]


def sum_for_list(L):
    P = list(chain((prime_factors(abs(n)) for n in L)))
    zP = list(zip(L, P))
    sP = sorted(set((p for l in P for p in l)))
    return [[p, sum((e[0] for e in zP if p in e[1]))] for p in sP]
