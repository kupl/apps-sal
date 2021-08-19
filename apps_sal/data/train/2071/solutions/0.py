from collections import Counter
n = int(input())
points = Counter([tuple(map(int, input().split(' '))) for i in range(n)])
(x, y) = (Counter([k for (k, v) in points.elements()]), Counter([v for (k, v) in points.elements()]))
ans = sum([v * (v - 1) // 2 for (k, v) in list(x.items())]) + sum([v * (v - 1) // 2 for (k, v) in list(y.items())]) - sum([v * (v - 1) // 2 for (k, v) in list(points.items())])
print(ans)
