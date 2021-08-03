from itertools import combinations
t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    x = list(map(int, input().split(maxsplit=n)))
    y = list(combinations(x, k))
    z = []
    for i in range(len(y)):
        z.append(sum(y[i]))
    print(z.count(min(z)))
