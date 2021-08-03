import math


def logBase2(n):
    res = 0
    fact = 1
    while((fact << (res + 1)) <= n):
        res += 1
    return res


t = int(input())

a = [-1, 0, 1]

for i in range(58):
    temp = a[-1] + a[-2]
    temp = temp % 10
    a.append(temp)
for _ in range(t):
    n = int(input())

    n = 1 << int(math.log2(n))

    print(a[n % 60])
