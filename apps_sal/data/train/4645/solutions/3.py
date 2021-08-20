def promenade(choices):
    x = [(1, 0), (0, 1)]
    for c in choices:
        x[c == 'R'] = (x[0][0] + x[1][0], x[0][1] + x[1][1])
    return (x[0][0] + x[1][0], x[0][1] + x[1][1])
