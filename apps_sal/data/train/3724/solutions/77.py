def hero(bullets, dragons):
    if bullets >= dragons * 2:
        return True
    if bullets <= dragons * 2:
        return False
