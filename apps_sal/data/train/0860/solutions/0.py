import math
T = int(input())
for _ in range(T):
    N, H = map(int, input().split())
    A = list(map(int, input().split()))
    low, high = 1, max(A)
    while low != high:
        time = 0
        mid = (low + high) // 2
        for i in range(N):
            time += math.ceil(A[i] / mid)

        if time <= H:
            high = mid
        else:
            low = mid + 1
    print(high)
