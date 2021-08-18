import math
for i in range(int(input())):
    n, v1, v2 = list(map(int, input().split()))
    t = ((math.sqrt(2) * n) / v1)
    e = ((2 * n) / v2)
    if e < t:
        print("Elevator")
    else:
        print("Stairs")
