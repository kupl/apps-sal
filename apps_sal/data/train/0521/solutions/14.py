import math
T = int(input())
for i in range(T):
    n = int(input())
    A = [int(k) for k in input().split()]
    A.sort()
    P, Q = [int(j) for j in input().split()]

    def angle(x1, x2, x, y):
        y = math.atan((x2 - x) / y) + math.atan((x - x1) / y)
        return y
    c = 0
    for i in range(n // 2):
        c = c + angle(A[i], A[n - i - 1], P, Q)

    print(c)
