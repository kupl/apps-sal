def hero(bullets, dragons):
    if bullets == 0:
        return False
    return bullets/dragons >= 2
