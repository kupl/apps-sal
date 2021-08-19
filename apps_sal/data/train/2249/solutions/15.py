q = int(input())
for _ in range(q):
    (x1, y1, x2, y2) = map(int, input().split())
    if x1 == x2:
        print(abs(y2 - y1))
    elif y1 == y2:
        print(abs(x2 - x1))
    else:
        print(abs(x2 - x1) + abs(y2 - y1) + 2)
