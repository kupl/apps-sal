from functools import partial, reduce
from itertools import chain
from operator import xor
calc_parity = partial(reduce, xor)


def correct(m, n, bits):
    bits = list(map(int, bits))
    xs = [bits[i * n:(i + 1) * n] for i in range(m)]
    row_parity = bits[m * n:-n]
    col_parity = bits[-n:]
    invalid_row = invalid_col = -1
    for (i, (row, p)) in enumerate(zip(xs, row_parity)):
        if calc_parity(row) != p:
            invalid_row = i
            break
    xs = [list(col) for col in zip(*xs)]
    for (i, (col, p)) in enumerate(zip(xs, col_parity)):
        if calc_parity(col) != p:
            invalid_col = i
            break
    xs = [list(col) for col in zip(*xs)]
    if invalid_row >= 0 <= invalid_col:
        xs[invalid_row][invalid_col] = 1 - xs[invalid_row][invalid_col]
    elif invalid_row >= 0:
        row_parity[invalid_row] = 1 - row_parity[invalid_row]
    elif invalid_col >= 0:
        col_parity[invalid_col] = 1 - col_parity[invalid_col]
    return ''.join(map(str, chain(chain.from_iterable(xs), row_parity, col_parity)))
