def hero(bullets, dragons):
    if bullets == 0:
        return False
    if bullets < dragons * 2:
        return False
    return True
