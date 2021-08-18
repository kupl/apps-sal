def solve(N, As):
    all_xor = 0
    for A in As:
        all_xor ^= A
    ans = ''
    for A in As:
        ans += str(A ^ all_xor) + ' '
    print((ans[:-1]))


def __starting_point():
    N = int(input())
    As = [int(i) for i in input().split()]
    solve(N, As)


__starting_point()
