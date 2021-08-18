def cost(x, y):
    return (abs(x[0] - y[0]) + abs(x[1] - y[1]))


def find(z):
    nonlocal p
    a = []
    while p[z] != z:
        a.append(z)
        z = p[z]
    for i in a:
        p[i] = z
    return z


class Solution:
    def minCostConnectPoints(self, a: List[List[int]]) -> int:
        nonlocal p
        n = len(a)
        b = []
        p = [i for i in range(n + 1)]
        s = [1 for i in range(n + 1)]
        for i in range(n):
            for j in range(i + 1, n):
                b.append((i, j, cost(a[i], a[j])))

        b.sort(key=lambda x: x[2])
        su = 0
        for i in b:
            x = find(i[0])
            y = find(i[1])
            if x != y:
                su += i[2]
                if s[x] > s[y]:
                    p[y] = x
                    s[x] += s[y]
                else:
                    p[x] = y
                    s[y] += s[x]
        return su
