from collections import Counter
(x, y, p) = (Counter(), Counter(), Counter())
for _ in range(int(input())):
    (i, j) = map(int, input().split())
    x[i] += 1
    y[j] += 1
    p[i, j] += 1


def cnt(n):
    return n * (n - 1) // 2


ans = sum(map(cnt, x.values())) + sum(map(cnt, y.values())) - sum(map(cnt, p.values()))
print(ans)
