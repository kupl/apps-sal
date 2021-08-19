n = int(input())
(x, y) = zip(*sorted((sorted(map(int, input().split())) for _ in range(n))))
a = x[-1]
b = d = 2 * 10 ** 9
for i in range(n - 1):
    a = max(a, y[i])
    b = min(b, y[i])
    d = min(d, a - min(b, x[i + 1]))
print(min((x[-1] - x[0]) * (max(y) - min(y)), (max(y) - x[0]) * d))
