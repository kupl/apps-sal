def make_2d_list(head, row, col):
    return [[]] if col == 0 else [list(x) for x in zip(*[iter(range(head, head + row * col))] * col)]
