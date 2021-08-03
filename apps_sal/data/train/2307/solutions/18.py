def main():
    N, A, B = list(map(int, input().split()))
    X = list(map(int, input().split()))

    ans = 0
    for i in range(N - 1):
        length = X[i + 1] - X[i]
        ans += min(length * A, B)

    print(ans)


def __starting_point():
    main()


__starting_point()
