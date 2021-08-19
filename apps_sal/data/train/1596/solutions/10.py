# cook your dish here
import math


def jump(x, t=1):
    if x <= 0:
        return t + x
    n = int(math.log(x + 1, 2))
    n = x - 2**n
    return jump(n, t + 1)


t = int(input())
for _ in range(t):
    x, y = list(map(int, input().split()))
    x = jump(x)
    y = jump(y)
    if x == y:
        print("0 0")
    elif x > y:
        print(2, x - y)
    else:
        print(1, y - x)
