(aa, bb, dp) = ([], [], [])


def dot(i, a):
    return dp[i] + a * bb[i]


def main():
    n = int(input())
    a = list(map(int, input().split(' ')))
    b = list(map(int, input().split(' ')))
    for k in range(n):
        dp.append(0)
        aa.append(a[k])
        bb.append(b[k])
    (st, i, j) = ([0 for _ in range(n)], 0, 0)
    for k in range(1, n):
        while j - i > 0 and dot(st[i], a[k]) >= dot(st[i + 1], a[k]):
            i += 1
        dp[k] = a[k] * b[st[i]] + dp[st[i]]
        while j - i > 0 and (b[st[j]] - b[k]) * (dp[st[j]] - dp[st[j - 1]]) > (dp[k] - dp[st[j]]) * (b[st[j - 1]] - b[st[j]]):
            j -= 1
        j += 1
        st[j] = k
    print(dp[-1])


def __starting_point():
    main()


__starting_point()
