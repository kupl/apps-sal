def hero(bullets, dragons):
    x = bullets / dragons
    if x == 2:
        return True
    elif bullets / 2 > dragons:
        return True
    else:
        return False
