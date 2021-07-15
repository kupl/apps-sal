def cup_and_balls(b, a):
    for l, r in a:
        b = r if b == l else l if b == r else b
    return b
