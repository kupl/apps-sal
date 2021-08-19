from sys import stdin, stdout
(n, m, k) = map(int, stdin.readline().split())
a = [0]
a = a + list(map(int, stdin.readline().split()))
op = [0]
mn = [0] * (m + 2)
kp = [0] * (n + 2)
for i in range(m):
    op.append(list(map(int, stdin.readline().split())))
for i in range(k):
    (x, y) = map(int, stdin.readline().split())
    mn[x] += 1
    mn[y + 1] -= 1
for i in range(1, m + 1):
    mn[i] += mn[i - 1]
    op[i][2] *= mn[i]
    kp[op[i][0]] += op[i][2]
    kp[op[i][1] + 1] -= op[i][2]
for i in range(1, n + 1):
    kp[i] += kp[i - 1]
for i in range(1, n + 1):
    print(str(a[i] + kp[i]), end=' ')
