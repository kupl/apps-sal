n, a, b = map(int, input().split())
xx = list(map(int, input().split()))
tired = 0
for i in range(n - 1):
    if (xx[i + 1] - xx[i]) * a < b:
        tired += (xx[i + 1] - xx[i]) * a
    else:
        tired += b

print(tired)
