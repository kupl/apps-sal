for _ in range(int(input())):
    N = list(map(int, input().split()))
    N.sort()
    N1, N2, N3 = N[0], N[1], N[2]
    M = 10**9 + 7
    ans = ((((N1 % M) * ((N2 - 1) % M)) % M) * (N3 - 2) % M) % M
    print(ans)
