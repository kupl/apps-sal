def solve():
    n = int(input())
    k = n // 2
    for i in range(n):
        j = 0
        if i <= k:
            z = i
        else:
            z = n - i - 1
        while j != z:
            print(" ", end="")
            j += 1
        print("*")


def __starting_point():
    T = int(input())
    for i in range(T):
        (solve())


__starting_point()
