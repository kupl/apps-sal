def make_2d_list(head, row, col):
    r = []
    x = head
    for _ in range(row):
        r.append(list(range(x, x + col)))
        x += col
    return r
