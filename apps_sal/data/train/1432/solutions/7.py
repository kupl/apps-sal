try:
    T = int(input())
    nsw = []
    for _ in range(T):
        N = int(input())
        a = []
        for __ in range(N):
            a += list(map(int, input().rstrip().split()))
        count = 0
        for ___ in a:
            if 1 == ___:
                count += 1
        count = count - N
        ans = 0
        while count > 0:
            ans += 1
            count = count - 2 * (N - 1)
            N = N - 1
        nsw += [ans]
    print('\n'.join(map(str, nsw)))
except EOFError:
    pass
