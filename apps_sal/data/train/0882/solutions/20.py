def soln():
    a = input()
    b = input()
    a1 = set(a)
    c = 0
    for i in a1:
        if i in b:
            c += min(a.count(i), b.count(i))

    print(c)


def main():
    t = int(input())
    while t > 0:
        t = t - 1
        soln()


def __starting_point():
    main()


__starting_point()
