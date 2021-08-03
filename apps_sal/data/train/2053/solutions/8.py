n, m = list(map(int, input().split()))
b = list(map(int, input().split()))
g = list(map(int, input().split()))
b = sorted(b, reverse=True)
g = sorted(g, reverse=True)
s = 0
if min(g) < max(b):
    print(-1)
else:
    for i in b:
        s += i * m
    c = m - 1
    k = 0
    for i in g:
        if i == b[k]:
            continue
        if c == 0:
            k += 1
            c = m - 1
        if c != 0 and i > b[k]:
            c -= 1
            s += i - b[k]
    print(s)
