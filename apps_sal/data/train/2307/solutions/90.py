def solve():
    (N, A, B) = map(int, input().split())
    X = list(map(int, input().split()))
    ans = 0
    for i in range(1, N):
        dx = X[i] - X[i - 1]
        if dx * A < B:
            ans += dx * A
        else:
            ans += B
    print(ans)


def __starting_point():
    solve()


__starting_point()
