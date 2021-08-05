def count_ways(s, indx, n):
    if indx == n:
        return 1

    if s[indx] == '0':
        return 0

    if dp[indx] != -1:
        return dp[indx]

    ans = count_ways(s, indx + 1, n) % 1000000007

    if n - indx >= 2 and (int(s[indx:indx + 2]) <= 26):
        ans += count_ways(s, indx + 2, n) % 1000000007
        ans %= 1000000007

    dp[indx] = ans
    return ans


t = int(input())

while t:
    t -= 1

    s = input()

    dp = [-1] * len(s)

    print(count_ways(s, 0, len(s)))
