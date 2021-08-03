def scratch(lottery):
    return sum(win(*line.split()) for line in lottery)


def win(a, b, c, d):
    return int(d) if a == b == c else 0
