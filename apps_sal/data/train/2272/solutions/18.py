from bisect import bisect_left, bisect_right

def solve():
    maxD = 30

    N = int(input())
    As = list(map(int, input().split()))
    Bs = list(map(int, input().split()))

    As.sort()
    Bs.sort()

    ans = 0
    for d in reversed(list(range(maxD))):
        m1 = 1 << d

        iA = bisect_left(As, m1)
        iB = bisect_left(Bs, m1)

        num1 = N * (N-iA + N-iB)

        As = As[:iA] + [A-m1 for A in As[iA:]]
        Bs = Bs[:iB] + [B-m1 for B in Bs[iB:]]

        As.sort()
        Bs.sort(reverse=True)

        iB = 0
        for A in As:
            while iB < N and A + Bs[iB] >= m1:
                iB += 1
            num1 += iB

        Bs.reverse()

        if num1 % 2:
            ans |= m1

    print(ans)


solve()

