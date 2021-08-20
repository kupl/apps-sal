import math
z = int(input())
for _ in range(z):
    [x, r, a, b] = [int(y) for y in input().split()]
    if x * min(a, b) == max(a, b):
        print(x - 2)
    elif x * abs(b - a) % max(a, b) == 0:
        print(math.floor(x * abs(a - b) / max(a, b)) - 1)
    else:
        print(math.floor(x * abs(a - b) / max(a, b)))
