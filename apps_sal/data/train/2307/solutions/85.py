(N, A, B, *X) = map(int, open(0).read().split())
print(sum((min(A * (y - x), B) for (x, y) in zip(X, X[1:]))))
