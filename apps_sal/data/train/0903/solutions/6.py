n = int(input())
for i in range(n):
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    if(x1 > x2):
        t = x1
        x1 = x2
        x2 = t
        t1 = y1
        y1 = y2
        y2 = t1
    r = y1 * (x2 - x1)
    r1 = r / (y2 + y1)
    print(x1 + r1)
