import sys
input = sys.stdin.readline
(inp, ip) = (lambda: int(input()), lambda: [int(w) for w in input().split()])
n = inp()
x = ip()
x.sort(reverse=True)
flag = 1
for i in range(n - 2):
    if x[i] < x[i + 1] + x[i + 2]:
        flag = 0
        print('YES')
        print(x[i], x[i + 1], x[i + 2])
        break
if flag:
    print('NO')
