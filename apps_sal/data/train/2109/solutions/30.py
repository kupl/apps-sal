import math
Q = int(input())
for roop in range(Q):
    (X, Y) = list(map(int, input().split()))
    A = min([X, Y])
    B = max([X, Y])
    if A == B:
        print(2 * A - 2)
    elif A + 1 == B:
        print(2 * A - 2)
    else:
        C = int(math.sqrt(A * B))
        while True:
            if C ** 2 >= A * B:
                C -= 1
            elif (C + 1) ** 2 < A * B:
                C += 1
            else:
                break
        if C * (C + 1) >= A * B:
            print(2 * C - 2)
        else:
            print(2 * C - 1)
