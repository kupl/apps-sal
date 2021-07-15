def hero(bullets, dragons):
    if dragons == 0:
        return True
    return True if bullets // dragons >= 2 else False
