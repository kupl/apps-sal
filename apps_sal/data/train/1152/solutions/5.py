n = int(input())
s = []
a = []
for i in range(n):
    (si, vi) = input().split()
    vi = int(vi)
    a.append(vi)
    s.append(si)
q = int(input())
for j in range(0, q):
    qi = input()
    ma = -20000000009
    pos = -1
    for k in range(0, n):
        if s[k].startswith(qi):
            if a[k] > ma:
                pos = k
                ma = a[k]
    if pos == -1:
        print('NO')
    else:
        print(s[pos])
