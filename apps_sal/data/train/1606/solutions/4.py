def __starting_point():
    (l, r) = list(map(int, input().split()))
    if l == r:
        print(l)
    else:
        print(2)


__starting_point()
