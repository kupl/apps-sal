from collections import Counter

def solve(files):
    c = Counter(f[f.rfind("."):] for f in files)
    MAX = max(c.values(), default=0)
    return sorted(e[0] for e in c.items() if e[1] == MAX)
