def hero(bullets, dragons):
    survive = True  # survive check
    temp_bullets = bullets / 2  # div bullets shott one dragon
    if temp_bullets >= dragons:  # if avalible bullets >= dragons then hero win else loose
        survive = True
    else:
        survive = False
    return survive  # return survive
