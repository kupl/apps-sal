from sys import stdin
import math
# Input data
#stdin = open("input", "r")


def func(x):
    count = 0
    while(x > 0):
        n = int(math.log2(x + 1))
        k = 2**n
        count += 1
        if k > x:
            k //= 2
        x -= k
    return count


for _ in range(int(stdin.readline())):
    x, y = list(map(int, stdin.readline().split()))
    a, b = func(x + 1), func(y + 1)
    if a == b:
        print(0, 0)
    else:
        if a > b:
            print(2, a - b)
        else:
            print(1, b - a)
