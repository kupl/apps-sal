import math
T = int(input())
for _ in range(T):
    N, H = map(int, input().split())
    A = list(map(int, input().split()))
    low = 1
    high = max(A)
    ans = 1
    while low <= high:
        time = 0
        mid = low + (high - low) // 2
        for i in range(N):
            time += int((A[i] + mid - 1) / mid)

        if time <= H:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    print(ans)
