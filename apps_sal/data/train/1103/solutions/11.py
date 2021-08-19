import math


def forloop(list):
    r = 1
    for x in list:
        r *= x
    return r


t = int(input())
while t > 0:
    l1 = []
    n = int(input())
    l = list(map(int, input().split()))
    for i in range(2, 1000000):
        l1.append(i * i)
    l1 = tuple(l1)
    n1 = forloop(l)
    for i in l1:
        if n1 % i == 0:
            break
    ans = math.sqrt(i)
    print(int(ans))
    t -= 1
