t = int(input())
for _ in range(t):
    n, d = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()

    low, high = 0, arr[-1] + d
    while (high - low) > 0.0000005:
        mid = (high + low) / 2
        time = arr[0] + mid
        ans = True
        for i in range(1, n):
            if arr[i] > time:
                time = arr[i]
                time += mid
            elif arr[i] <= time <= arr[i] + d:
                time += mid
            else:
                ans = False
                break
        if ans:
            low = mid
        else:
            high = mid

    print(low)
