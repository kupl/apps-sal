def hero(bullets, dragons):

    def teki(dragons):
        return 2 * dragons
    if bullets > teki(dragons):
        return True
    elif bullets == teki(dragons):
        return True
    else:
        return False
