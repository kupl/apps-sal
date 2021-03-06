import sys


def input():
    return sys.stdin.readline().strip()


def main():
    mod = 998244353
    (N, K) = list(map(int, input().split()))
    '\n    １を使うか使わないかで場合分けする発想はどうして出てくるんだ。。。\n    再帰構造が見える感じ？？？\n    再帰で実装すると間に合わなかったのでdpテーブルで実装。\n    dp[n][k] = dp[n - 1][k - 1] + dp[n][k * 2]\n    '
    dp = [[0] * (N * 2 + 5) for _ in range(N + 1)]
    dp[0][0] = 1
    dp[1][1] = 1
    for n in range(1, N + 1):
        for k in range(n, -1, -1):
            dp[n][k] = dp[n - 1][k - 1] + dp[n][k * 2]
            dp[n][k] %= mod
    print(dp[N][K])


def __starting_point():
    main()


__starting_point()
