3


def main():
    N = int(input())
    A = input()
    B = input()
    d = {(0, 0): 0, (0, 1): 0, (1, 0): 0, (1, 1): 0}
    c = 0
    for i in range(N):
        a = int(A[i])
        b = int(B[i])
        c += d[a, b]
        if (a, b) == (0, 0):
            d[1, 0] += 1
            d[1, 1] += 1
        elif (a, b) == (0, 1):
            d[1, 0] += 1
        elif (a, b) == (1, 0):
            d[0, 0] += 1
            d[0, 1] += 1
        else:
            d[0, 0] += 1
    print(c)


def __starting_point():
    main()


__starting_point()
