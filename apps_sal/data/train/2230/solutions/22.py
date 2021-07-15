import operator

n = int(input())
p = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
input()
c = list(map(int, input().split()))

t = sorted(zip(p, a, b), key=operator.itemgetter(0))
t = [list(x) for x in t]
p = [None, 0, 0, 0]

r = []
for ci in c:
    i = p[ci]
    while i < n and ci not in (t[i][1], t[i][2]):
        i += 1
    if i == n:
        r.append(-1)
    else:
        r.append(t[i][0])
        t[i][1], t[i][2] = 0, 0
        i += 1
    p[ci] = i
print(' '.join(map(str, r)))

