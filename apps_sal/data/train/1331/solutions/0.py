from math import log, ceil, floor
t = int(input())
while t:
    t -= 1
    (n, k) = map(int, input().split())
    v = floor(log(k, 2))
    block = 1 << v + 1
    print(n / block * (1 + (k - 2 ** v) * 2))
