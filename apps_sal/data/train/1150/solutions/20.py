import math
t = int(input())
for _ in range(t):
    a = int(input())
    x1 = math.floor(math.sqrt(a))
    x2 = a - x1 * x1
    c = 0
    while 1:
        c = c + 1
        if x2 == 0:
            print(c)
            break
        x1 = math.floor(math.sqrt(x2))
        x2 = x2 - x1 * x1
