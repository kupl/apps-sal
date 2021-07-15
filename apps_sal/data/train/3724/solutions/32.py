def hero(bullets, dragons):
    required = dragons * 2
    if required > bullets:
        return False
    else:
        return True

