def gimme(inp):
    a = max(inp)
    b = min(inp)
    for i in range(len(inp)):
        if b < inp[i] < a:
            return i
