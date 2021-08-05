import math


t = int(input().strip())

for _ in range(t):
    n, m = list(map(int, input().strip().split()))
    a = []
    v = [-1] * 4

    for i in range(n):
        a.append(input().strip())

    for i, ai in enumerate(a):
        if ai.find('*') > -1:
            v[2] = i
            break

    if v[2] == -1:
        print(0)
    else:

        for i, ai in reversed(list(enumerate(a))):
            if ai.find('*') > -1:
                v[3] = i
                break

        for i in range(m):
            x = [ai[i] for ai in a]
            if '*' in x:
                v[0] = i
                break

        for i in reversed(range(m)):
            x = [ai[i] for ai in a]
            if '*' in x:
                v[1] = i
                break

        if v.count(v[0]) == len(v):
            print(1)
        else:
            print(int(math.ceil(max(v[3] - v[2], v[1] - v[0]) / 2.0)) + 1)
