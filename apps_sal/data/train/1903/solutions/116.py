parent = 0


def find(i):
    nonlocal parent
    l1 = []
    while parent[i] != i:
        l1.append(i)
        i = parent[i]
    j = i
    for i in l1:
        parent[i] = j
    return j


def givedistance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


class Solution:
    def minCostConnectPoints(self, l: List[List[int]]) -> int:
        nonlocal parent

        visited = {}

        l1 = []
        n = len(l)
        for i in range(n):
            for j in range(i + 1, n):
                l1.append([givedistance(l[i], l[j]), tuple(l[i]), tuple(l[j])])

        l1.sort()
        l1.reverse()

        ans = 0

        if n == 1:
            return 0

        d = {}
        ind = 0
        for i in l:
            d[tuple(i)] = ind
            ind += 1

        for i in range(len(l1)):
            l1[i][1] = d[l1[i][1]]
            l1[i][2] = d[l1[i][2]]
        parent = {}
        for i in l1:
            parent[i[1]] = i[1]
            parent[i[2]] = i[2]

        taken = 0
        while taken != n - 1:
            curr, i, j = l1.pop()

            p1 = find(i)
            p2 = find(j)

            if p1 != p2:
                parent[p1] = parent[p2]
                ans += curr
                taken += 1
        return ans
