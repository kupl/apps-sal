def main():

    t = int(input())

    for i in range(t):
        a = str(input())
        b = str(input())
        checkJewellery(a, b)


def checkJewellery(a, b):
    count = 0
    for s in b:
        if s in a:
            count = count + 1
    print(count)


def __starting_point():
    main()


__starting_point()
