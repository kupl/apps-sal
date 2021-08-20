from math import sqrt
Q = int(input())
for i in range(Q):
    (A, B) = map(int, input().split())
    m = A * B
    C = int(sqrt(m))
    if C * C == m:
        C = C - 1
    if A == B or B == A + 1:
        ans = 2 * A - 2
    elif A == B + 1:
        ans = 2 * B - 2
    elif C * (C + 1) < m:
        ans = 2 * C - 1
    else:
        ans = 2 * C - 2
    print(ans)
