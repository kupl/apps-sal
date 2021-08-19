from math import sqrt


def list_squared(m, n):
    squares = []
    for i in range(m, n):
        i_squares = 0
        for j in range(1, int(sqrt(i) // 1) + 1):
            if i % j == 0:
                i_squares += j ** 2
                if i // j != j:
                    i_squares += (i // j) ** 2
        if i_squares % sqrt(i_squares) == 0 and i_squares / sqrt(i_squares) == sqrt(i_squares):
            squares.append([i, i_squares])
    return squares
