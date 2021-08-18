import math
t = int(input())
while t > 0:
    n = int(input())
    k = n + 1
    k *= 2
    a = math.sqrt(k)
    a = int(a)
    if a * (a + 1) > k:
        a -= 1
    b = k - (a * (a + 1))
    if b == 0:
        c = a - 1
    else:
        c = b // 2
        c -= 1
    print(c)
    t -= 1
