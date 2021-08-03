squares = {x**2 for x in range(10)}


def square_sums_row(n):
    def rec(x, L):
        if not L:
            return x and [x]
        for i, y in enumerate(L):
            if x == 0 or x + y in squares:
                test = rec(y, L[:i] + L[i + 1:])
                if test:
                    return (x and [x] or []) + test
        return False
    return rec(0, list(range(1, n + 1)))
