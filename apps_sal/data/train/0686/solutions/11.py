import math
for t in range(int(input())):
    n, v1, v2 = map(int, input().split())
    t2 = (2 * n) / v2
    t1 = (math.sqrt(2) * n) / v1
    if t1 <= t2:
        print("Stairs")
    else:
        print("Elevator")
