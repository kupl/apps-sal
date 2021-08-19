def solve():
    n = int(input())
    it = n
    k = 1
    for i in range(n):
        j = 0
        while j < it:
            print(k, end='')
            j += 1
            k += 1
        print('')
        it -= 1


def __starting_point():
    T = int(input())
    for i in range(T):
        solve()


__starting_point()
