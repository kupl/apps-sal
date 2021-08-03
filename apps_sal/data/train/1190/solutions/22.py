T = int(input())
ans = []


def fun1(p, i):
    n = int(p / (2**i))
    return p - (n * (2**i))


def fun2(p, i):
    n = int(p / (2**i))
    return n


ans = []
for x in range(T):
    p = int(input())
    sum = 0
    for y in range(11, -1, -1):
        sum = sum + fun2(p, y)
        p = fun1(p, y)
    ans.append(sum)
for z in ans:
    print(z)
