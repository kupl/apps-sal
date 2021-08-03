import math

for t in range(int(input())):
    mod = 1000000007
    pro = 1
    a, b = list(map(int, input().split()))
    for i in range(a):
        if(i == 0):
            pro *= b
        else:
            pro *= ((b - 1))
            if(pro > mod):
                pro %= mod
    print(pro % mod)
