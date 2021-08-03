# dt = {} for i in x: dt[i] = dt.get(i,0)+1
import sys
input = sys.stdin.readline
inp, ip = lambda: int(input()), lambda: [int(w) for w in input().split()]

for _ in range(inp()):
    a = ip()
    b = ip()
    d = [0] * 3
    for i in range(3):
        d[i] = b[i] - a[i]
    ans = 0
    flag = 0
    for i in d:
        if i < 0:
            flag = 1
            break
        elif i > 0:
            ans += i
    if flag:
        print(-1)
    else:
        print(ans)
