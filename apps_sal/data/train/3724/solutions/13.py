def hero(bullets, dragons):
    while bullets > 0:
        if bullets / dragons >= 2:
            return True
        break
    return False
