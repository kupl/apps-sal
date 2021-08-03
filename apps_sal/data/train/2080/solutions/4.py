def main():
    input()
    q = min(list(map(int, input().split())))
    input()
    aa = sorted(map(int, input().split()), reverse=True)
    print(sum(aa) - sum(aa[q::q + 2]) - sum(aa[q + 1::q + 2]))


def __starting_point():
    main()


__starting_point()
