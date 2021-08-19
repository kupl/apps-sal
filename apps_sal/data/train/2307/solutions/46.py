def resolve():
    (N, A, B) = map(int, input().split())
    X = list(map(int, input().split()))
    ans = 0
    for i in range(N - 1):
        res = min((X[i + 1] - X[i]) * A, B)
        ans += res
    print(ans)


def __starting_point():
    resolve()


__starting_point()
