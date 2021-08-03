from sys import stdin, stdout
input = stdin.readline
n = int(input())
a = [[] for i in range(n)]
for i in range(n - 1):
    u, v = map(int, input().split())
    a[u - 1].append(v - 1)
    a[v - 1].append(u - 1)
b = [0] * n
vis = [0] * n
st = [(0, 0)]
vis[0] = 1
pa = [0] * n
while st:
    x, y = st.pop()
    b[x] = y
    for i in a[x]:
        if vis[i] == 0:
            pa[i] = x
            vis[i] = 1
            if x == 0:
                st.append((i, y + len(a[x]) - 1))
            else:
                st.append((i, y + len(a[x]) - 2))
c = []
for i in range(1, n):
    if len(a[i]) == 1:
        c.append((b[i], i))
c.sort()
ans = 0
while c:
    x, y = c.pop()
    m = y
    p = 0
    while y != 0 and pa[y] != -1:
        y = pa[y]
        if pa[y] == -1:
            break
        if y != 0:
            p += (len(a[y]) - 2)
        else:
            p += (len(a[y]) - 1)
    if p >= 1:
        p = 0
        while m != 0 and pa[m] != -1:
            x = m
            if pa[m] == -1:
                break
            m = pa[m]
            pa[x] = -1
            if m != 0:
                p += (len(a[m]) - 2)
            else:
                p += (len(a[m]) - 1)
        if y == 0:
            pa[0] = -1
for i in range(n):
    if pa[i] != -1:
        st = [i]
        pa[i] = -1
        while st:
            x = st.pop()
            for j in a[x]:
                if pa[j] != -1:
                    pa[j] = -1
                    st.append(j)
        ans += 1
print(ans)
