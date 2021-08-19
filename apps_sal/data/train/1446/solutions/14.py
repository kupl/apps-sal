import math


def Log2(x):
    if x == 0:
        return false
    return math.log10(x) / math.log10(2)


def isPowerOfTwo(n):
    return math.ceil(Log2(n)) == math.floor(Log2(n))


for _ in range(int(input())):
    n = int(input())
    m = n + 1
    if n == 1:
        print('2')
    elif isPowerOfTwo(m):
        print(n // 2)
    else:
        print('-1')
