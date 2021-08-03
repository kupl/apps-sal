import sys
input = sys.stdin.readline


def solve():
    INF = float('inf')

    N = int(input())
    Ls = []
    Rs = []
    for _ in range(N):
        x, y = list(map(int, input().split()))
        if x > y:
            x, y = y, x
        Ls.append(x)
        Rs.append(y)

    minAll = min(Ls)
    maxAll = max(Rs)

    ans1 = (max(Ls) - minAll) * (maxAll - min(Rs))

    ans2 = INF
    LRs = []
    min1, max1 = INF, -INF
    for L, R in zip(Ls, Rs):
        if L != minAll:
            if R != maxAll:
                LRs.append((L, R))
            else:
                min1 = min(min1, L)
                max1 = max(max1, L)
        else:
            if R != maxAll:
                min1 = min(min1, R)
                max1 = max(max1, R)
            else:
                print(ans1)
                return

    if not LRs:
        print(ans1)
        return

    LRs.sort()

    d1 = maxAll - minAll
    maxL = LRs[-1][0]
    minR, maxR = INF, -INF
    ans2 = INF
    for L, R in LRs:
        minL = L
        diff = max(maxL, maxR, max1) - min(minL, minR, min1)
        ans2 = min(ans2, d1 * diff)
        minR = min(minR, R)
        maxR = max(maxR, R)

    minL, maxL = INF, -INF
    diff = max(maxL, maxR, max1) - min(minL, minR, min1)
    ans2 = min(ans2, d1 * diff)

    print((min(ans1, ans2)))


solve()
