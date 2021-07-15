def hero(bullets, dragons):
    survival = None
    if dragons == 0:
        survival = True
    elif bullets/dragons >= 2:
        survival = True
    else:
        survival = False
    return survival
