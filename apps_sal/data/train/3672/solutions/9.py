def solve(Q): return sum(1 + F if 1 & int(V) else 0 for F, V in enumerate(Q))
