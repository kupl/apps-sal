t = int(input())


def power(x, y):
    res = 1     # Initialize result

    # Update x if it is more
    # than or equal to p
    x = x % mod

    while (y > 0):

        # If y is odd, multiply
        # x with result
        if ((y & 1) == 1):
            res = (res * x) % mod

        # y must be even now
        y = y >> 1      # y = y/2
        x = (x * x) % mod

    return res


# Driver Code

for tc in range(t):
    n, m1 = input().split()
    n, m1 = int(n), int(m1)
    print("Case " + str(tc + 1) + ":")
    for i in range(m1):
        s = input()
        k = len(s)
        mod = 10**9 + 7
        m = n - k
        if k > n:
            print(0)
        else:
            # print((n-k+1)*(26**(n-k)))%(10**9+7)
            print(((m + 1) * power(26, m)) % mod)
