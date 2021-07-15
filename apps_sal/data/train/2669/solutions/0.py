from operator import mul
from functools import reduce

def genSequence(n):
    yield n
    while True:
        n += reduce(mul, [int(d) for d in str(n) if d != '0']) if n > 9 else n
        yield n

def extract(seq, v):
    return sorted(seq).index(v)

def convergence(n):
    gen1, genN = genSequence(1), genSequence(n)
    seq1, seqN = {next(gen1)}, {next(genN)}
    while True:
        a,b = next(gen1), next(genN)
        seq1.add(a)
        seqN.add(b)
        if a in seqN: return extract(seqN, a)
        if b in seq1: return extract(seqN, b)
