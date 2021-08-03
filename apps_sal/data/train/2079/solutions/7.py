w = {}


def up(a, b, d):
    while a != b:
        if a < b:
            a, b = b, a
        if a not in w:
            w[a] = 0
        w[a] += d
        a = a // 2


def get(a, b):
    res = 0
    while a != b:
        if a < b:
            a, b = b, a
        if a in w:
            res += w[a]
        a = a // 2
    return res


q = int(input())
for i in range(q):
    a = [int(b) for b in input().split()]
    if a[0] == 1:
        up(a[1], a[2], a[3])
    else:
        print(get(a[1], a[2]))
