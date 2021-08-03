import operator
n = int(input())
p = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
m = int(input())
c = list(map(int, input().split()))

l = [list() for i in range(1, 4)]

for i in range(n):
    l[a[i] - 1].append((p[i], i))
    if a[i] != b[i]:
        l[b[i] - 1].append((p[i], i))

l = list(map(lambda l_: sorted(l_, key=operator.itemgetter(0)), l))
invalid = set()
ys = [0] * 4


for i in range(m):
    y = ys[c[i] - 1]
    while (y < len(l[c[i] - 1])) and (l[c[i] - 1][y][1] in invalid):
        y += 1
    if y == len(l[c[i] - 1]):
        print(-1, end=' ')
    else:
        print(l[c[i] - 1][y][0], end=' ')
        invalid.add(l[c[i] - 1][y][1])
    ys[c[i] - 1] = y
