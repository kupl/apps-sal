import math
t = int(input())
for i in range(t):
    x1, y1, x2, y2 = map(int, input().split())
    if math.sqrt(pow(x1, 2) + pow(y1, 2)) > math.sqrt(pow(x2, 2) + pow(y2, 2)):
        print("B IS CLOSER")
    else:
        print("A IS CLOSER")
