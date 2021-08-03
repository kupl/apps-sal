import math
t = int(input())
while(t > 0):
    x1, y1, x2, y2 = input().split()
    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)
    d1 = math.sqrt((x1)**2 + (y1)**2)
    d2 = math.sqrt((x2)**2 + (y2)**2)
    if(d1 < d2):
        ans = 'A'
    else:
        ans = 'B'
    print(ans, 'IS CLOSER')
    t = t - 1
