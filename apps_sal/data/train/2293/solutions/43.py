import sys
input = sys.stdin.readline


def I(): return int(input())
def MI(): return list(map(int, input().split()))
def LI(): return list(map(int, input().split()))


def main():
    mod = 10**9 + 7
    N = I()
    A = LI()
    N2 = pow(2, N)

    """
    下位集合に対する高速ゼータ変換．
    (Kがi,jを包含している）
    ここでのgを適切なfの和として考えるのが基本だけど，
    今回は和ではなくて上位2つの要素を持つ
    """

    g = [[0, 0]for _ in range(N2)]

    for i in range(N2):
        g[i][0] = A[i]

    for k in range(N):
        for s in range(N2):
            if ((s >> k) & 1):
                L = [0, 0, 0, 0]
                L[0] = g[s][0]
                L[1] = g[s][1]
                L[2] = g[(s ^ (1 << k))][0]
                L[3] = g[(s ^ (1 << k))][1]
                L.sort()
                g[s][0] = L[-1]
                g[s][1] = L[-2]

    ans = 0
    for k in range(1, N2):
        ans = max(ans, sum(g[k]))
        print(ans)


main()
