import math
import collections
for z in range(int(input())):
    a = [tuple for i in range(3)]
    A = list(map(int, input().strip().split()))
    X, Y = 0, 0
    j = 0
    for i in range(3):
        x, y = A[2 * i], A[2 * i + 1]
        X += x
        Y += y
        j += 1
    Z = - X
    if X > 0:
        X -= (X // 3)
    else:
        X += (2 - X) // 3
    Z = - Y
    if Y > 0:
        Y -= (Y // 3)
    else:
        Y += (2 - Y) // 3
    if X == 1 and Y == 1:
        print((0))
    elif X == 2 and Y == 2:
        print((1))
    elif X == Y:
        print((max(abs(X - 1), abs(Y - 1)) + 1))
    else:
        print((max(abs(X - 1), abs(Y - 1))))
