import math
n = int(input())
for _ in range(n):
    x = input().split()
    x1 = int(x[0])
    y1 = int(x[1])
    x2 = int(x[2])
    y2 = int(x[3])
    d2 = math.sqrt((x2**2) + (y2**2))
    d1 = math.sqrt((x1**2) + (y1**2))
    if d1 < d2:
        print("A IS CLOSER")
    else:
        print("B IS CLOSER")
