def arr_str(arr):
    strr = ""
    for i in arr:
        strr += str(i)
    return(strr)


for _ in range(int(input())):
    n, m = map(int, input().split())
    A = [0] * n
    for i in range(n):
        temp = [0]
        B = [int(i) for i in input().split()]
        temp.extend(B)
        temp.append(0)
        A[i] = temp

    ans = [[0 for i in range(m)] for j in range(n)]
    dp = [[0 for i in range(m + 2)] for j in range(n)]
    for i in range(m):
        dp[0][i + 1] = A[0][i + 1]
    for i in range(1, n):
        for j in range(1, m + 1):
            temp = max(dp[i - 1][j - 1], dp[i - 1][j], dp[i - 1][j + 1])
            if(temp > A[i][j]):
                ans[i - 1][j - 1] = 0
            else:
                ans[i - 1][j - 1] = 1
            temp = max(temp, A[i][j])
            dp[i][j] = temp
    tem = [1] * m

    print(arr_str(tem), end="\n")
    for i in range(n - 1):
        print(arr_str(ans[i]), end="\n")
