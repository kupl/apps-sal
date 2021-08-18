dp = [[-1 for i in range(505)] for j in range(505)]
n = int(input())
A = [int(i) for i in input().split()]


def do(i, j):
    if i >= j:
        dp[i][j] = 1
        return 1

    if dp[i][j] != -1:
        return dp[i][j]

    ans = len(A)
    if A[i] == A[j]:
        ans = min(ans, do(i + 1, j - 1))
    for x in range(i, j):

        left = do(i, x)
        right = do(x + 1, j)
        ans = min(ans, left + right)

    dp[i][j] = ans
    return ans


if len(set(A)) == n:
    print(n)
else:
    print(do(0, n - 1))
