from itertools import combinations
for i in range(int(input())):
    n, k = map(int, input().split())
    x = list(map(int, input().split(maxsplit=n)))
    y = list(combinations(x, k))
    z = []
    for i in range(len(y)):
        z.append(sum(y[i]))
    print(z.count(min(z)))
