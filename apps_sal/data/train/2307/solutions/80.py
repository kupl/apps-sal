(n, a, b, *x) = map(int, open(0).read().split())
print(sum([min(b, a * (x[i + 1] - x[i])) for i in range(n - 1)]))
