def hero(bullets, dragons):
    if (bullets / 2) > dragons :
        return True
    elif bullets == 0:
        return False
    else:
        return bullets % dragons == 0 and bullets / dragons == 2
