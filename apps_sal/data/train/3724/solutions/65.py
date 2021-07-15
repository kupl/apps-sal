def hero(bullets, dragons):
    survive = True
    if bullets / 2 >= dragons:
        survive = True
    else:
        survive = False
    return survive
