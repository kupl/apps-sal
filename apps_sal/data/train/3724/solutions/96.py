def hero(bullets, dragons):
    # if there are twice as many bullets as dragons, or more;
    if bullets >= 2 * dragons:
        return True
    else:
        return False
