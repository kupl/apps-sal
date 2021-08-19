# cook your dish here
def printGift(n):
    dim = 2 * n - 1
    start = 0
    end = dim - 1
    a = [[0 for i in range(10000)]for i in range(10000)]
    while n != 0:
        for i in range(start, end + 1):
            for j in range(start, end + 1):
                if i == start or i == end or j == start or j == end:
                    a[i][j] = n

        start += 1
        end -= 1
        n -= 1

    for i in range(dim):
        for j in range(dim):
            print(a[i][j], end=" ")
        print()


def __starting_point():
    n = int(input())
    printGift(n)


__starting_point()
