def hero(bullets, dragons):  # function
    if bullets >= dragons * 2:  # number of bullets should be greater than or equal to twice the number of dragons
        return True
    else:
        return False
