from itertools import product
def coin(n): return list(map("".join, product(*(['HT'] * n))))
