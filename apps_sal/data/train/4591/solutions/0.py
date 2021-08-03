def how_many_bees(h):
    if not h:
        return 0
    v = list(zip(*h))
    b = [None] * len(h)
    sf = (b[i:] + l + b[:i] for i, l in enumerate(h))
    sb = (b[:i] + l + b[i:] for i, l in enumerate(h))
    df = [[n for n in l if n is not None] for l in zip(*sf)]
    db = [[n for n in l if n is not None] for l in zip(*sb)]
    inline = '\n'.join(map(''.join, h + v + df + db))
    return (inline + inline[::-1]).count('bee')
