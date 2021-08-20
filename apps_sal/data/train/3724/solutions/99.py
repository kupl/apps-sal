def hero(bullets, dragons):
    x = dragons * 2
    if x <= bullets:
        return True
    else:
        return False
