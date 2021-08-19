import math
n = int(input())
d = [0] * 200200
a = [0]
s = 0
ans = []
for i in range(n):
    x = tuple(map(int, input().split()))
    if x[0] == 1:
        d[x[1]] += x[2]
        s += x[1] * x[2]
    elif x[0] == 2:
        a.append(x[1])
        s += x[1]
    else:
        cc = len(a)
        s -= d[cc] + a.pop()
        d[cc - 1] += d[cc]
        d[cc] = 0
    ans.append(str(s / len(a)))
print('\n'.join(ans))
