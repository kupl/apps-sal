
from math import gcd


def func(ind, g, dp, n, a):

    # Base case
    if (ind == n):
        if (g == 1):
            return 1
        else:
            return 0

    # If already visited
    if (dp[ind][g] != -1):
        return dp[ind][g]

    # Either we take or we do not
    ans = (func(ind + 1, g, dp, n, a) +
           func(ind + 1, gcd(a[ind], g),
           dp, n, a))

    # Return the answer
    dp[ind][g] = ans
    return dp[ind][g]


def countSubsequences(a, n):

    # Hash table to memoize
    dp = [[-1 for i in range(MAX)]
          for i in range(n)]

    # Count the number of subsequences
    count = 0

    # Count for every subsequence
    for i in range(n):
        count += func(i + 1, a[i], dp, n, a)

    return count


t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    MAX = max(l) + 1
    print(countSubsequences(l, n))
