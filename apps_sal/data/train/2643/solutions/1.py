def __starting_point():
    n = int(input().strip())
    english = set(map(int, input().strip().split(' ')))
    m = int(input().strip())
    french = set(map(int, input().strip().split(' ')))
    print(len(english.symmetric_difference(french)))


__starting_point()
