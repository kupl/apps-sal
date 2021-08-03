import itertools


def minl(l):
    return l[-1] if len(l) > 0 else 10**9 + 1


input()
p = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
input()
c = list(map(int, input().split()))

d = [[[] for _ in range(3)] for _ in range(3)]
for pi, ai, bi in zip(p, a, b):
    d[ai - 1][bi - 1].append(pi)

for row in d:
    for l in row:
        l.sort(reverse=True)

r = []
for ci in c:
    ci -= 1
    row = ((ci, j) for j in range(3))
    col = ((i, ci) for i in range(3))
    i, j = min(itertools.chain(row, col),
               key=lambda p: minl(d[p[0]][p[1]]))
    l = d[i][j]
    r.append(l.pop() if len(l) > 0 else -1)
print(*r, sep=' ')
