def hero(bullets, dragons):
    if dragons:
        return True if bullets / dragons >= 2.0 else False
    else:
        return True
