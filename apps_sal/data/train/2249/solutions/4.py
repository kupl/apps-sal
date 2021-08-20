import math
T = int(input())
for t in range(T):
    (x1, y1, x2, y2) = list(map(int, input().split()))
    d = False
    print(abs(x1 - x2) + abs(y2 - y1) + 2 * ((y2 != y1) * (x2 != x1)))
