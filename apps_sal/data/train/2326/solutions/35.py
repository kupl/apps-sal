def main():
    N, *A = map(int, open(0).read().split())
    L, C = {}, {}
    for i, a in enumerate(A):
        if a in C:
            C[a] += 1
        else:
            C[a] = 1
            L[a] = i
    Z = [0] * N
    B = sorted(C, reverse=True)
    l = N - 1
    cnt = 0
    for b, c in zip(B, B[1:] + [0]):
        l = min(l, L[b])
        cnt += C[b]
        Z[l] += (b - c) * cnt
    print(*Z, sep="\n")


def __starting_point():
    main()


__starting_point()
