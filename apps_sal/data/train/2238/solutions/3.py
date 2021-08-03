def main():
    for _ in range(int(input())):
        l, r = list(map(int, input().split()))
        mask = 1
        while l <= r:
            x = l
            l |= mask
            mask <<= 1
        print(x)


def __starting_point():
    main()


__starting_point()
