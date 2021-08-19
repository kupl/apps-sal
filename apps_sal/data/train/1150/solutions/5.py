import math
try:
    t = int(input())
    for i in range(t):
        c = -0
        x = int(input())
        while x != 0:
            x -= math.floor(math.sqrt(x)) ** 2
            c += 1
        print(c)
except:
    pass
