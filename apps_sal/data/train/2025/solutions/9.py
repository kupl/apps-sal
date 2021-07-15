def main():
    n = int(input()) + 1
    a, res = [True] * n, []
    for p in range(2, n):
        if a[p]:
            pp = 1
            while pp * p < n:
                pp *= p
                res.append(pp)
            a[p:n:p] = [False] * ((n - 1) // p)
    print(len(res))
    print(*res)


def __starting_point():
    main()

__starting_point()
