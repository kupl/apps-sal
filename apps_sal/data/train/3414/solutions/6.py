from re import sub


def reversi_row(moves):
    base = "........"
    point = "*"
    for move in moves:
        base = list(base)
        base[move] = "#"
        base = "".join(base)
        base = sub("#O+\*", lambda m: "*" * len(m.group(0)), sub("\*O+#", lambda m: "*" * (len(m.group(0)) - 1) + "#", base)) if point == "*" else sub("#\*+O", lambda m: "O" * len(m.group(0)), sub("O\*+#", lambda m: "O" * (len(m.group(0)) - 1) + "#", base))
        base = base.replace("#", point)
        point = 'O' if point == "*" else '*'
    return base
