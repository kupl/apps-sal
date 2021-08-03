from math import *
t = int(input())
for i in range(t):
    a, b, c, d = list(map(int, input().split()))
    y = abs(c - d)
    x = abs(a - b)
    if(y == 0):
        if(x == 0):
            print("YES")
        else:
            print("NO")
        continue

    x = x / y
    if(ceil(x) == floor(x)):
        print("YES")
    else:
        print("NO")
