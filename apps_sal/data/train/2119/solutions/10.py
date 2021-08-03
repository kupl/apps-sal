n = int(input())
a = list(map(int, input().split()))
d = list(map(int, input().split()))
q = [[i, i, -1] for i in range(n)]
o = ['0']
m = -1
for i in reversed(d[1:]):
    i -= 1
    q[i][2] = a[i]
    l, r = i, i
    if i < n - 1 and q[i + 1][2] != -1:
        r = q[i + 1][1]
        q[r][2] += a[i]
    if i > 0 and q[i - 1][2] != -1:
        l = q[i - 1][0]
        q[l][2] += a[i]
    q[l][1] = r
    q[r][0] = l
    q[l][2] += q[r][2] - a[i]
    q[r][2] = q[l][2]
    m = max(m, q[r][2])
    o.append(str(m))
print('\n'.join(reversed(o)))
