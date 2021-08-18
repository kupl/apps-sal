from itertools import permutations
for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = [False] * (n + 1)
    for i in a:
        if i != 0:
            b[i] = True
    g = []
    grd = 0
    for i in range(1, n + 1):
        if not b[i]:
            g.append(i)
    for i in permutations(g):
        b = a[:]
        f = 0
        ff = list(i[:])
        for j in range(n):
            if b[j] == 0:
                b[j] = ff[-1]
                ff.pop()
        for j in range(1, n):
            if b[j] > b[j - 1]:
                f += 1
        if f == k:
            grd += 1
    print(grd)
