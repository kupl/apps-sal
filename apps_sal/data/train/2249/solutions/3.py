T = int(input())

for t in range(T):
    x1, y1, x2, y2 = [int(_) for _ in input().split()]
    if x1 == x2 or y1 == y2:
        print(abs(x2-x1) + abs(y2-y1))
    else:
        print(abs(x2-x1) + abs(y2-y1) + 2)

