# cook your dish here
def array1(size):
    return [0 for _ in range(size)]


def array2(rows, cols):
    return [[0 for _ in range(cols)] for _ in range(rows)]


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    no_of_twos = array1(n + 1)
    for i in range(n - 1, -1, -1):
        if a[i] == 1:
            no_of_twos[i] = 0
        else:
            no_of_twos[i] += 1
            no_of_twos[i] += no_of_twos[i + 1]
    dp = array1(n + 1)
    dp[0] = 1
    ans = 1
    for i in range(1, n):
        if i - 1 >= 0:
            dp[i] += dp[i - 1]
        if i - 2 >= 0 and a[i - 2] == 2:
            dp[i] += dp[i - 2]
        if i - 3 >= 0 and a[i - 3] == 2 and a[i - 2] == 2:
            dp[i] += dp[i - 3]
        dp[i] = dp[i] % 1000000007
        ans += dp[i]
        x = no_of_twos[i + 1]
        if i + 1 < n and a[i - 1] == 2:
            ans += (x * dp[i - 1])
            if x % 2 == 0:
                if i + x + 1 < n:
                    ans += dp[i - 1]
                if i + x + 2 < n and a[i + x + 2] == 2:
                    ans += dp[i - 1]
        ans = ans % 1000000007
    print(ans % 1000000007)
