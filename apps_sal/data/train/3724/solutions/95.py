def hero(bullets, dragons):
    return False if dragons == 0 or bullets / dragons < 2 else True
