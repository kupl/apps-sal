def hero(bullets, dragons):
    return False if dragons == 0 else True if bullets / dragons >= 2 else False
