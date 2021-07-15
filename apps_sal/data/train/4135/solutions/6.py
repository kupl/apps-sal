from collections import Counter

def solve(s):
    c = Counter(s)
    l, cc, mi, ma, su = len(c), Counter(c.values()), min(c.values()), max(c.values()), sum(c.values())
    return (
        len(c) == 1
        or su - ma * l == 1
        or mi == 1 == su - ma * l + ma
        or cc[ma] == 1 == ma - mi
    )
