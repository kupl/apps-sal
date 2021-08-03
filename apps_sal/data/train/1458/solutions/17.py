# cook your dish here

def countSquares(n):
    return sum([(n - i + 1) ** 2 for i in range(1, n + 1, 2)])


def __starting_point():
    t = int(input())
    for i in range(t):
        n = int(input())
        print(countSquares(n))


__starting_point()
