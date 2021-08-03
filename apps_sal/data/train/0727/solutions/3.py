NumOfTests = int(input())

pwrOfTwo = [2, 4, 8, 16]

for test in range(NumOfTests):
    N, M = input().split()
    N = int(N)
    M = int(M)

    if N == 1:
        used_m = 2
        m_div = M - used_m
        if m_div < 0:
            print(-1)
        else:
            print(m_div)
    else:
        x, y = divmod(N, 2)

        max_p = x * (N + 3) + y * (N + 3) / 2

        max_pwr = max([x for x in pwrOfTwo if N + 1 >= x])

        min_p = (N + 1) * (pwrOfTwo.index(max_pwr) + 1) + 2 * (N + 1 - max_pwr)

        if min_p > M:
            print(-1)
        elif M <= max_p:
            print(0)
        else:
            print(M - max_p)
