def check(seq, elem):
    marker = False
    for _ in seq:
        if elem == _:
            return True
    return marker
