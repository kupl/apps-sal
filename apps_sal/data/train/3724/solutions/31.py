def hero(bullets, dragons):
    if bullets > dragons:
        if bullets // dragons >= 2:
            return True
        else:
            return False
    else:
        return False
