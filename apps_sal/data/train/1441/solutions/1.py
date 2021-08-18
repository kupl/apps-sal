for t in range(int(input())):
    n, k = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))
    arr.append(-1)
    arr = arr[::-1]
    x = arr.index(max(arr))
    dp = [0] * (n + 1)
    for i in range(1, n + 1, 1):
        for l in brr:
            if i - l < 0:
                continue
            elif i - l < x and x <= i:
                dp[i] = 1
            else:
                dp[i] |= not dp[i - l]
    if dp[n]:
        print("Chef")
    else:
        print("Garry")
