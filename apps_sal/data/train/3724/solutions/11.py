def hero(bullets: int, dragons: int) -> bool:
    """
    Can the hero survive?
        It takes 2 bullets to kill a dragon
    Parameters:
        bullets (int): number of bullets
        dragons (int): number of dragons
    Returns:
        True (Lives) or False (Dies)
    """
    return bullets >= (dragons * 2)
