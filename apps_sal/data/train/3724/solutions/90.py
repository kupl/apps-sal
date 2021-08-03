def hero(bullets, dragons):
    if dragons >= bullets:
        return False
    elif bullets >= dragons + dragons:
        return True
    else:
        return False
