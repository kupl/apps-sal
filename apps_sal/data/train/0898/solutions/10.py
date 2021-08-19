import math
for ad in range(int(input())):
    (m, n) = list(map(int, input().split()))
    a = m
    c = len(str(n))
    if n != int(c * '9'):
        c -= 1
    b = c * a
    print(str(b) + ' ' + str(a))
