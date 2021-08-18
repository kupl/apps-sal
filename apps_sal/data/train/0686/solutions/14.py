import math
T = int(input())
for i in range(T):
    n, v1, v2 = list(map(int, input().split()))
    x = v1 * math.sqrt(2) * n
    y = v2 * n
    if x < y:
        print("Elevator")
    else:
        print("Stairs")
