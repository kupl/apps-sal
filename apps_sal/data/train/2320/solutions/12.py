def main():
    n = int(input())
    aa = sorted(map(int, input().split()), reverse=True)
    bb = list(map(int, input().split()))
    ij = sorted(list(range(n)), key=bb.__getitem__)
    for (i, j) in enumerate(ij):
        bb[j] = aa[i]
    print(' '.join(map(str, bb)))


def __starting_point():
    main()


__starting_point()
