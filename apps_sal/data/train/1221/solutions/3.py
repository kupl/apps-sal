import math
T = int(input())
for i in range(T):
    x = int(input())
    (temp, count, y) = (0, 0, 0)
    p = 0
    while temp <= x:
        p = int(math.sqrt(y))
        if p * p > y:
            temp = p
            y += p * p
            count += 1
        else:
            p += 1
            temp = p
            y += p * p
            count += 1
    if temp > x:
        print(count - 1)
    elif temp <= x:
        print(count)
