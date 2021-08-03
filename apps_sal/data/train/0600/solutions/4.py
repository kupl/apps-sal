import math

t = int(input())

a = [-1, 0, 1]

for i in range(61):
    temp = a[-1] + a[-2]
    temp = temp % 10
    a.append(temp)

for _ in range(t):
    n = int(input())

    n = int(math.log(n, 2))

    n = (2**n) % 60
    print(a[n])
