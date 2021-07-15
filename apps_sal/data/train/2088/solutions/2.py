def main():
    n, l = int(input()), list(map(int, input().split()))
    dp = [[0] * n for _ in range(n + 1)]
    for le in range(1, n + 1):
        for lo, hi in zip(list(range(n)), list(range(le - 1, n))):
            row, c = dp[lo], l[lo]
            if le == 1:
                row[hi] = 1
            else:
                tmp = [1 + dp[lo + 1][hi]]
                if c == l[lo + 1]:
                    tmp.append(1 + dp[lo + 2][hi])
                for match in range(lo + 2, hi + 1):
                    if c == l[match]:
                        tmp.append(dp[lo + 1][match - 1] + dp[match + 1][hi])
                row[hi] = min(tmp)
    print(dp[0][n - 1])


def __starting_point():
    main()

__starting_point()
