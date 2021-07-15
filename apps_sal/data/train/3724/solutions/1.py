def hero(bullets, dragons):
    '''
    Ascertains if hero can survive
    Parameters:
        bullets: (int) - number of bullets hero has
        dragons: (int) - number of dragons
    Returns:
        True (Survive) or False (Hero gets killed)
    '''
    if bullets >= 2*dragons:
        return True
    elif bullets < 2*dragons:
        return False

