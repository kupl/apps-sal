def correct(m, n, bits):
    def parities(matrix): return [sum(row) & 1 for row in matrix]
    def wrong_index(a, b): return next((i for i, (x, y) in enumerate(zip(a, b)) if x ^ y), None)

    bits = list(map(int, bits))
    message, row_par, col_par = bits[:-m - n], bits[-m - n:-n], bits[-n:]
    rows = list(zip(* [iter(message)] * n))

    actual_row, actual_col = parities(rows), parities(zip(*rows))
    idx_row, idx_col = wrong_index(row_par, actual_row), wrong_index(col_par, actual_col)

    if idx_row is not None and idx_col is not None:
        message[idx_row * n + idx_col] = message[idx_row * n + idx_col] ^ 1
    elif idx_row is not None:
        row_par[idx_row] = row_par[idx_row] ^ 1
    elif idx_col is not None:
        col_par[idx_col] = int(col_par[idx_col]) ^ 1

    return ''.join(map(str, message + row_par + col_par))
