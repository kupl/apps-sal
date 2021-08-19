import math


def cal_gcd(a):
    first = a[0]
    for i in range(1, len(a)):
        first = math.gcd(first, a[i])
    return first


for _ in range(int(input())):
    n = int(input())
    a = list(set(map(int, input().split())))
    n = len(a)
    if n == 1:
        print(2 * a[0])
    else:
        a.sort(reverse=True)
        b1 = a[0]
        b2 = a[1]
        if n >= 3:
            first = a[2]
            for i in range(3, len(a)):
                first = math.gcd(first, a[i])
            print(max(b1 + math.gcd(first, b2), b2 + math.gcd(first, b1)))
        else:
            print(b1 + b2)
