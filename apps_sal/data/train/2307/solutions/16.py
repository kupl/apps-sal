(n, a, b, *X) = map(int, open(0).read().split())
print(sum((min(a * (X[i + 1] - X[i]), b) for i in range(n - 1))))
