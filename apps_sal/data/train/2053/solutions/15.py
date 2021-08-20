def R():
    return map(int, input().split())


(n, m) = R()
a = list(R())
b = list(R())
a.sort()
b.sort()
t = sum(a) * m + sum(b) - a[-1] * m
if a[-1] > b[0]:
    print(-1)
elif a[-1] == b[0]:
    print(t)
else:
    print(t + a[-1] - a[-2])
