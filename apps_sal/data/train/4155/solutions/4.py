table = str.maketrans('69', '96', '23457')


def solve(a, b):
    return sum((1 for n in range(a, b) if f'{n}'[::-1] == f'{n}'.translate(table)))
