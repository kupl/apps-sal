from collections import Counter
t = int(input())
for _ in range(t):
    n = int(input())
    x = Counter()
    y = Counter()
    for i in range(4 * n - 1):
        (a, b) = map(int, input().split())
        x.update([a])
        y.update([b])
    for i in x.keys():
        if x[i] % 2 != 0:
            p = i
            break
    for j in y.keys():
        if y[j] % 2 != 0:
            q = j
            break
    print(p, q)
