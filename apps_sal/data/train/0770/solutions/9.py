def sol(b, k):
    l = len(b)
    if l == 0:
        return 0
    elif l == 1:
        return A[b[0]]
    n = b[-1]
    dp = [0] * (n + 1)
    dp[n] = A[n]
    x = 2
    ret = 0
    for i in range(n - 1, -1, -1):
        if i > b[l - x]:
            dp[i] = dp[i + 1]
        elif i < b[0]:
            ret = dp[i + 1]
            break
        else:
            if i + k + 1 > n:
                dp[i] = max(A[i], dp[i + 1])
            else:
                dp[i] = max(A[i] + dp[i + k + 1], dp[i + 1])
            x += 1
    if ret:
        return ret
    return dp[0]


for _ in range(int(input())):
    (n, k) = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]
    (odd, even) = ([], [])
    for i in range(len(A)):
        if A[i] % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    ans = sol(odd, k) + sol(even, k)
    print(ans)
