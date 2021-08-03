from math import log
def score(n): return 2**int(1 + log(n, 2)) - 1 if n else 0
