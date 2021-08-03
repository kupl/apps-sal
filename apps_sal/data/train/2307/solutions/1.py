n, a, b, *X = map(int, open(0).read().split())
c = 0
for x0, x1 in zip(X, X[1:]):
    c += min(a * (x1 - x0), b)
print(c)
