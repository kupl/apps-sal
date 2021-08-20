def make_2d_list(head, row, col):
    return [list(range(i, i + col)) for i in range(head, head + row * col, col)] if col else [[]]
