t = int(input())

for i in range(t):
    x1, y1, x2, y2 = list(map(int, input().split()))
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    if dx == 0 and dy == 0:
        print(0)
    elif dx == 0 or dy == 0:
        print(max(dx, dy))
    else:
        print(dx + dy + 2)
