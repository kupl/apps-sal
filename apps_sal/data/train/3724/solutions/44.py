def hero(bullets, dragons):
    if dragons != 0:
        return bullets / dragons >= 2
    elif bullets != 0:
        return False
    return True
