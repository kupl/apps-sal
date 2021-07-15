def main():
    n = int(input())

    if n == 1:
        print("1")
        print("1")
        return
    elif n == 2:
        print("1")
        print("1 1")
        return
    elif n == 3:
        print("2")
        print("1 1 2")
        return
    else:
        numbers = [True] * (n+3)
        for prime in range(2, n+3):
            for i in range(2 * prime, n+3, prime):
                numbers[i] = False

        print(2)
        print(" ".join([str(1) if numbers[i+2] else str(2) for i in range(n)]))


def __starting_point():
    main()

__starting_point()
