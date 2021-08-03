import sys


def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    A = [int(a) for a in input().split()]
    if M < sum(A):
        print(0)
        return 0
    mod = 7 + 10 ** 9

    Ans = 1
    sumA = sum(A)
    for i in range(sumA + N):
        Ans *= (M + N - i)
        Ans %= mod
    fact = 1
    for i in range(1, sumA + N + 1):
        fact *= i
        fact %= mod
    Ans *= pow(fact, mod - 2, mod)
    print(Ans % mod)

    return 0


def __starting_point():
    solve()


__starting_point()
