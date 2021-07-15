func = lambda n: sum(map(int, str(n)))

# Fuck it, brute-force
def min_and_max(l, d, x):
    while func(l) != x: l += 1
    while func(d) != x: d -= 1
    return [l, d]
