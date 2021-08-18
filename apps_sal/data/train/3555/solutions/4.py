def hanoiArray(n):

    def move(n, source, target, auxiliary):
        if n > 0:
            move(n - 1, source, auxiliary, target)

            target.append(source.pop())

            res.append([A[:], B[:], C[:]])

            move(n - 1, auxiliary, target, source)

    A = list(range(n, 0, -1))
    B = []
    C = []

    res = [[A[:], B[:], C[:]]]

    move(n, A, C, B)
    return '\n'.join(map(str, res))
