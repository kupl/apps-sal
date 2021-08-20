def solve():
    mod = 10 ** 9 + 7
    (N, M) = map(int, input().split())
    A = list(map(int, input().split()))
    M += N
    S = sum(A) + N
    if S > M:
        print(0)
        return
    ans = 1
    d = 1
    for i in range(1, S + 1):
        ans = ans * (M + 1 - i) % mod
        d = d * i % mod
    ans = ans * pow(d, mod - 2, mod) % mod
    '\n    for i in range(1,S+1):\n        ans = (ans*(M+1-i)) % mod\n        d = pow(i,mod-2,mod)\n        ans = (ans*d) % mod\n    '
    print(ans)


def __starting_point():
    solve()


__starting_point()
