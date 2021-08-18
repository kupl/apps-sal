import sys
input = sys.stdin.readline
inp, ip = lambda: int(input()), lambda: [int(w) for w in input().split()]

n = inp()
x = ip()
m = inp()
for i in range(m):
    ind, pos = ip()
    ind -= 1
    t = x[ind]
    x[ind] = 0
    if ind >= 1:
        x[ind - 1] += pos - 1
    if ind <= n - 2:
        x[ind + 1] += t - pos
for i in range(n):
    print(x[i])
