t = int(input())
for w in range(t):
    n = int(input())
    l = l2 = []
    sm = 0
    l = [i for i in range(1, n + 1)]
    for a in range(n - 1, 0, -1):
        l.append(a)
    for p in l:
        sm = sm + p ** 3
    print(sm)
