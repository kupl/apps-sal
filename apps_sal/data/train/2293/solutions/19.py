def solve():
    N = int(input())
    As = list(map(int, input().split())) + [0]

    pow2 = 2**N

    anss = []
    ans = 0
    max2s = [[0, -1]]
    for S in range(1, pow2):
        m1, m2 = S, -1
        for i in range(N):
            if (S >> i) & 1:
                S0 = S ^ (1 << i)
                i1, i2 = max2s[S0]
                if m1 == i1:
                    m2 = m2 if As[m2] >= As[i2] else i2
                elif As[m1] >= As[i1]:
                    m2 = m2 if As[m2] >= As[i1] else i1
                else:
                    m2 = m1 if As[m1] >= As[i2] else i2
                    m1 = i1
        ans2 = As[m1] + As[m2]
        if ans2 > ans:
            ans = ans2
        anss.append(ans)
        max2s.append([m1, m2])

    print(('\n'.join(map(str, anss))))


solve()
