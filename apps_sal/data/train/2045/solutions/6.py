import os
(n, m) = list(map(int, input().split()))
parent = list(range(0, n + 1))
answer = list(range(0, n))


def getParent(x):
    while parent[x] != x:
        x = parent[x]
        parent[x] = parent[parent[x]]
    return parent[x]


for i in range(m):
    (l, r, x) = list(map(int, input().split()))
    cnt = getParent(l - 1)
    while cnt <= r - 1:
        if cnt == x - 1:
            cnt = cnt + 1
        else:
            parent[cnt] = cnt + 1
            answer[cnt] = x - 1
        cnt = getParent(cnt)
c = 0
s = ''
for i in answer:
    if c == i:
        s += '0 '
    else:
        s += str(i + 1) + ' '
    c = c + 1
os.write(1, str.encode(s))
