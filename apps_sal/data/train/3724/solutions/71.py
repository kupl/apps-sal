def hero(bullets, dragons):
    res = bullets / dragons
    if res >= 2:
        return True
    else:
        return False
