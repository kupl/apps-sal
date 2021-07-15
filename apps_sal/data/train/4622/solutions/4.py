def double_check(inp):
    inp = inp.lower()
    return any(i == j for i, j in zip(inp[:-1], inp[1:]))
