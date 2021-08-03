import math
T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    left = 0
    for i in range(N):
        v = A[i] - ans - left
        if (v < 0):
            left = -v
        else:
            ans = ans + math.ceil(v / (i + 1))
            left = (math.ceil(v / (i + 1)) * (i + 1)) - v

    print(ans)
