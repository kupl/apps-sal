import math as ma
for _ in range(int(input())):
    (m, n) = list(map(int, input().split()))
    count = 0
    l = int(ma.floor(ma.log(n, 10)))
    if n == pow(10, l + 1) - 1:
        l += 1
    print(m * l, m)
