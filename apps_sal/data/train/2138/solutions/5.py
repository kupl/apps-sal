def main():
    (a, b) = (input().count('1') for _ in 'ab')
    print(('NO', 'YES')[a + (a & 1) >= b])


def __starting_point():
    main()


__starting_point()
