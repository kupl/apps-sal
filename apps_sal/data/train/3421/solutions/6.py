from itertools import islice

def fib():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a+b

def mysterious_pattern(m, n):
    board = [[' '] * m for _ in range(n)]

    for i, x in enumerate(islice(fib(), m)):
        board[x % n][i] = 'o'
    return '\n'.join(''.join(row).rstrip() for row in board).strip('\n')
