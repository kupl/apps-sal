# ライブラリインポート
from collections import defaultdict

# 入力受け取り


def getlist():
    return list(map(int, input().split()))

# 処理内容


def main():
    S = list(input())
    N = len(S)
    s = [0] * (N + 1)
    for i in range(N):
        if S[i] == "A":
            s[i + 1] += s[i] + 2
        else:
            s[i + 1] += s[i] + 1
    T = list(input())
    M = len(T)
    t = [0] * (M + 1)
    for i in range(M):
        if T[i] == "A":
            t[i + 1] += t[i] + 2
        else:
            t[i + 1] += t[i] + 1
    Q = int(input())
    for i in range(Q):
        a, b, c, d = getlist()
        if ((s[b] - s[a - 1]) - (t[d] - t[c - 1])) % 3 == 0:
            print("YES")
        else:
            print("NO")


def __starting_point():
    main()


__starting_point()
