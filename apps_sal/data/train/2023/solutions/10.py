import itertools
3


def main():
    N = int(input())
    bestv = 4 * N
    besti = -1
    for i in range(1, N + 1):
        v = i + (N + i - 1) // i
        if v < bestv:
            bestv = v
            besti = i
    A = []
    cur = N
    if N % besti > 0:
        a = [cur - j for j in range(N % besti)]
        a.reverse()
        A.append(a)
        cur -= N % besti
    while cur > 0:
        a = [cur - j for j in range(besti)]
        a.reverse()
        A.append(a)
        cur -= besti
    print(*list(itertools.chain.from_iterable(A)))


def __starting_point():
    main()


__starting_point()
