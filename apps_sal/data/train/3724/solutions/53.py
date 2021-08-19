def hero(bullets, dragons):
    if dragons > 0:
        if bullets // dragons >= 2:
            return True
    return False
