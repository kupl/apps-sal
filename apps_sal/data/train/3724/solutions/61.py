def hero(bullets, dragons):
    if dragons != 0:
        return (bullets / dragons) >= 2
    else:
        return False
