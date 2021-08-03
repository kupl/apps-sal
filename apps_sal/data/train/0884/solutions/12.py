import math
t = int(input())
for cases in range(t):
    x, k = map(int, input().split())
    fx = []
    fk = []
    for i in range(2, x + 1):
        if(x % i == 0):
            fx.append(i)
    for i in range(2, k + 1):
        if(k % i == 0):
            fk.append(i)
    o1 = 0
    for i in fx:
        o1 += pow(i, k)
    o2 = 0
    for i in fk:
        o2 += i * x
    print(o1, o2)
