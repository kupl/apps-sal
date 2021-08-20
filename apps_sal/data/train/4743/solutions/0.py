def target_game(values):
    a = b = 0
    for n in values:
        (a, b) = (b, max(a + n, b))
    return max(a, b)
