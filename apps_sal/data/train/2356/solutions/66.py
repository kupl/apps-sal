import sys
def input(): return sys.stdin.readline().strip()


def main():
    mod = 998244353
    N, K = list(map(int, input().split()))
    """
    １を使うか使わないかで場合分けする発想はどうして出てくるんだ。。。
    再帰構造が見える感じ？？？
    再帰で実装すると間に合わなかったのでdpテーブルで実装。
    dp[n][k] = dp[n - 1][k - 1] + dp[n][k * 2]
    """
    dp = [[0] * (N * 2 + 5) for _ in range(N + 1)]  # dp[n][k] = (n個の要素でkを表す場合の数)
    dp[0][0] = 1
    dp[1][1] = 1
    
    for n in range(1, N + 1):
        for k in range(n, -1, -1):
            dp[n][k] = dp[n - 1][k - 1] + dp[n][k * 2]
            dp[n][k] %= mod
    #for n in range(N + 1): print(n, dp[n])
    
    print((dp[N][K]))

def __starting_point():
    main()





__starting_point()
