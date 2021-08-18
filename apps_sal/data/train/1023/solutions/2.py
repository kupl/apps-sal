def solve():
    n = int(input())
    it = 1
    k = 1
    for i in range(n):
        j = 0
        while j < it:
            mark = 1
            if (i == n - 1 or (j == 0 or j == it - 1)):
                print(k, end="")
                k += 1
            else:
                print(" ", end="")
            j += 1
        print("")
        it += 1


def __starting_point():
    T = int(input())
    for i in range(T):
        (solve())


__starting_point()
