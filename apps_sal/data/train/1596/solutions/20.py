def main():
    T = int(input())
    while T:
        (a, b) = list(map(int, input().split()))
        c1 = bin(a + 1).count('1')
        c2 = bin(b + 1).count('1')
        if c1 > c2:
            print(2, c1 - c2)
        elif c1 < c2:
            print(1, c2 - c1)
        else:
            print('0 0')
        T -= 1


def __starting_point():
    main()


__starting_point()
