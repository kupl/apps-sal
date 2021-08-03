n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
s = [[] for i in range(n)]
for i in range(m):
    inp = list(map(int, input().split()))
    s[inp[0] - 1].append(inp[1] - 1)
    s[inp[1] - 1].append(inp[0] - 1)
c = 0
d = [0 for i in range(n)]
for i in range(n):
    if d[i]:
        continue
    c += 1
    d[i] = c
    st = s[i]
    while st:
        ns = []
        for j in st:
            if d[j]:
                continue
            d[j] = c
            ns += s[j]
        st = ns
c = 0
for i in range(n):
    if d[i] == d[a[i] - 1]:
        c += 1
print(c)
