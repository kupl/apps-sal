def squares_needed(g):
    return 0 if g == 0 else int(__import__('math').log(g, 2) + 1)
