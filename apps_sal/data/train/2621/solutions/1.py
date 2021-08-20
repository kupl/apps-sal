def __starting_point():
    k = int(input().strip())
    numbers = list(map(int, input().strip().split(' ')))
    print((sum(set(numbers)) * k - sum(numbers)) // (k - 1))


__starting_point()
