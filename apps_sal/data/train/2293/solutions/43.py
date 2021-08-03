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

    for k in range(N):  # このkはKと違う，kbit目に着目する
        for s in range(N2):  # これが今回でいうK，
            if ((s >> k) & 1):  # sのkbit目が立っていれば
                # 加法として，上位2つを選択する
                L = [0, 0, 0, 0]
                L[0] = g[s][0]
                L[1] = g[s][1]
                L[2] = g[(s ^ (1 << k))][0]  # sのkbit目をマスクしたgを持ってくる
                L[3] = g[(s ^ (1 << k))][1]
                L.sort()
                g[s][0] = L[-1]
                g[s][1] = L[-2]
                # print(bin(s),k,g[s],L)

    ans = 0
    for k in range(1, N2):
        ans = max(ans, sum(g[k]))
        print(ans)


main()
