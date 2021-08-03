def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    tmp = A[-1]
    diff_A = [0] * N
    for i in range(N - 1, -1, -1):
        tmp = max(A[i], tmp)
        diff_A[i] = tmp - A[i]

    print(diff_A.count(max(diff_A)))


def __starting_point():
    main()


__starting_point()
