def extract(s):
    arr = []
    news = ''
    for x in s:
        try:
            x = int(x)
            news += str(x)
        except:
            arr += [news]
            news = ''
            arr += [x]
    arr += [news]
    return arr


t = int(input())
for _ in range(t):
    s = input()
    arr = extract(s)
    n = len(arr) // 2 + 1
    dp = [[0] * n for j in range(n)]
    for i in range(n):
        dp[i][i] = [int(arr[2 * i])]

    n = len(arr)
    for i in range(3, n + 1, 2):
        for j in range(0, n - i + 1, 2):
            ans = []
            for k in range(j + 2, i + j + 1, 2):
                for x in dp[j // 2][(k - 1) // 2]:
                    for y in dp[k // 2][(i + j) // 2]:
                        if arr[k - 1] == '&':
                            ans += [x & y]
                        if arr[k - 1] == '|':
                            ans += [x | y]
                        if arr[k - 1] == '^':
                            ans += [x ^ y]
            if i != n:
                dp[j // 2][k // 2] = ans[:]
            else:
                print(max(ans))
