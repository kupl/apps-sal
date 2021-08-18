
def solve():
    """
    スカーフをそれぞれs[1]...s[N]とする
    Nは偶数より、
    必ず a[1]^...^a[N] = s[1]^...^s[N] (=Sと置く) になる。

    よって、s[1]が求めたかったら、s[1] = S ^ a[1]で求められる。
    """
    import sys
    N = int(sys.stdin.readline())
    As = list(map(int, sys.stdin.readline().split()))

    S = 0
    for a in As:
        S ^= a

    anss = []
    for i in range(N):
        anss.append(str(S ^ As[i]))

    ans = " ".join(anss)
    print(ans)


def __starting_point():
    solve()


__starting_point()
