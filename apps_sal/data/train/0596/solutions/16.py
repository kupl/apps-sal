from math import *
t = int(input())
p = 1000000007
while(t):
    t -= 1
    x, k = list(map(int, input().split()))
    y = ceil(k / 2)
    if(x == 0):
        if(k == 1):
            print(0)
            continue
        k -= 1
        y = (k * (k + 1))
        y = y // 2
        y = y * 2
        print(y % p)
        continue
    if(k == 1):
        print((x * x) % p)
    elif(k == 2):
        z = x * x
        z += 2 * x
        print(z % p)
    elif(k % 2):
        minus = (x * (x + 1))
        minus = minus // 2
        fi = x * x
        y = x + (k // 2)
        fac = ((y * (y + 1)) // 2)
        fac -= minus
        fac = fac * 2
        fi += fac
        print(fi % p)
    else:
        minus = (x * (x + 1))
        minus = minus // 2
        se = (x * x) + (2 * x)
        y = x + ((k - 1) // 2)
        fac = ((y * (y + 1)) // 2)
        fac -= minus
        fac = fac * 2
        se += fac
        print(se % p)
