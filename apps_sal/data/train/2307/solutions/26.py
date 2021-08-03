n, a, b = list(map(int, input().split()))
xs = list(map(int, input().split()))

ans = sum([min((xs[i] - xs[i - 1]) * a, b) for i in range(1, n)])
print(ans)
