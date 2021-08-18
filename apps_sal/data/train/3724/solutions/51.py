def hero(bullets, dragons):
    survive = True
    temp_bullets = bullets / 2
    if temp_bullets >= dragons:
        survive = True
    else:
        survive = False
    return survive
