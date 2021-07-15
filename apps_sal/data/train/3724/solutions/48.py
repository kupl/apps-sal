def hero(bullets, dragons):
    if (bullets != 0 and bullets % dragons == 0) or (bullets != 0 and (bullets - 2 * dragons)) > 0:
        return True
    else:
        return False
