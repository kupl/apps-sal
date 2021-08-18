from re import sub


def reversi_row(moves):
    base = "........"
    point = "*"
    for move in moves:
        base = list(base)
        base[move] = "
        base = "".join(base)
        base = sub("
        base=base.replace("
        point='O' if point == "*" else '*'
    return base
