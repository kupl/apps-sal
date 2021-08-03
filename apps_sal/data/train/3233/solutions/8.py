def floyd(matrix, row, col):
    def f(row, col):
        return list(map(int, matrix[row][col].split(',')))
    x0 = [row, col]
    tortoise = f(*x0)
    hare = f(*f(*x0))
    while tortoise != hare:
        tortoise = f(*tortoise)
        hare = f(*f(*hare))

    mu = 0
    tortoise = x0
    while tortoise != hare:
        tortoise = f(*tortoise)
        hare = f(*hare)
        mu += 1

    lam = 1
    hare = f(*tortoise)
    while tortoise != hare:
        hare = f(*hare)
        lam += 1

    return lam if mu == 0 else -1


def robot_transfer(matrix, k):
    SIZE = len(matrix)
    return sum(1 for row in range(SIZE) for col in range(SIZE) if floyd(matrix, row, col) == k)
