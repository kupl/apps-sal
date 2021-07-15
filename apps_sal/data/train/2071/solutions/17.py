from collections import Counter

x, y, xy, ans = Counter(), Counter(), Counter(), 0
for i in range(int(input())):
    xi, yi = map(int, input().split())
    x[xi] += 1
    y[yi] += 1
    xy[(xi, yi)] += 1
for i in x:
    ans += x[i] * (x[i] - 1)
for i in y:
    ans += y[i] * (y[i] - 1)
for i in xy:
    ans -= xy[i] * (xy[i] - 1)
print(ans // 2)
