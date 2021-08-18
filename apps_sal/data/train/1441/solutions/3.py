for t in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    x = list(map(int, input().split()))

    wv = max(a)
    wvi = a.index(wv)

    dp = [False] * n
    dp[wvi] = True
    for i in range(wvi - 1, -1, -1):
        for j in x:
            if (i + j) > n:
                continue
            if (i + j) > wvi:
                dp[i] = True
            elif dp[i + j] == False:
                dp[i] = True
                break

    if dp[0]:
        print("Chef")
    else:
        print("Garry")
