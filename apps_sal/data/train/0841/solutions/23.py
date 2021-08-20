T = int(input())
for i in range(T):
    N = int(input())
    ans = N
    M = N
    L = len(str(N))
    ls = list(str(N))
    key = 10 ** L % (10 ** 9 + 7)
    for i in range(L - 1):
        a0 = int(ls[i])
        M = (10 * M + a0 * (1 - key)) % (10 ** 9 + 7)
        ans = (ans * key + M) % (10 ** 9 + 7)
    print(ans % (10 ** 9 + 7))
