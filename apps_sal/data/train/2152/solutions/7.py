from math import ceil
n = int(input())
x = list(map(int, input().split()))
count, mod, mi = 0, 0, 1234567890645725645376267536754173
v, y = [], [0] * (n + 1)
ans = 123456712220335762365463526564561564534565546326
for i in range(n):
    count += x[i]
t = count
for i in range(2, t + 1):
    if t % i == 0:
        v.append(i)
        while(t % i == 0):
            t //= i
for i2 in v:
    c = 0
    for i in range(n):
        y[i] = x[i]
    for i in range(n):
        if y[i] <= 0:
            y[i + 1] -= abs(y[i])
            c += abs(y[i])
        elif y[i] % i2 < i2 - y[i] % i2:
            y[i + 1] += y[i] % i2
            c += y[i] % i2
        else:
            y[i + 1] -= i2 - y[i] % i2
            c += i2 - y[i] % i2
    ans = min(ans, c)
if count == 1:
    print(-1)
else:
    print(ans)
