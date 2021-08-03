def hero(bullets, dragons):
    dead_dragons = bullets / 2
    if dragons > dead_dragons:
        return False
    else:
        return True
