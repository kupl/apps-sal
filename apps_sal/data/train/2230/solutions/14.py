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
    pm = 1000000001
    im = -1
    for j, l in enumerate(d[ci - 1]):
        if len(l) > 0 and l[-1] < pm:
            pm = l[-1]
            im = ci - 1
            jm = j
    for i, ll in enumerate(d):
        l = ll[ci - 1]
        if len(l) > 0 and l[-1] < pm:
            pm = l[-1]
            im = i
            jm = ci - 1
    r.append(d[im][jm].pop() if im >= 0 else -1)
print(*r, sep=' ')

