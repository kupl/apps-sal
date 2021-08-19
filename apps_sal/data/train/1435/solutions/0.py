import copy
n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
c = []
d = []
lcs = []


def lcsfn(a, c, corda, cordb):
    for i in range(n + 1):
        d.append([0] * (n + 1))
        lcs.append([0] * (n + 1))
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if a[i - 1] == c[j - 1]:
                lcs[i][j] = lcs[i - 1][j - 1] + 1
                d[i][j] = 'd'
            elif lcs[i - 1][j] > lcs[i][j - 1]:
                lcs[i][j] = lcs[i - 1][j]
                d[i][j] = 'u'
            else:
                lcs[i][j] = lcs[i][j - 1]
                d[i][j] = 'l'
    i = n
    j = n
    cost = 0
    while i >= 1 and j >= 1:
        if d[i][j] == 'd':
            corda.append(a[i - 1])
            cordb.append(b[j - 1])
            i -= 1
            j -= 1
            cost += 1
        elif d[i][j] == 'l':
            j -= 1
        elif d[i][j] == 'u':
            i -= 1
    return cost


ma = -10 ** 9
p1 = []
p2 = []
for i in range(-1000, 1001):
    c = []
    corda = []
    cordb = []
    for j in range(n):
        c.append(b[j] + i)
    p = lcsfn(a, c, corda, cordb)
    if ma < p:
        ma = p
        p1 = copy.deepcopy(corda)
        p1 = p1[::-1]
        p2 = copy.deepcopy(cordb)
        p2 = p2[::-1]
print(ma)
print(*p1)
print(*p2)
