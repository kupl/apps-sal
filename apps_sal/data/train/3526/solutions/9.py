def any_arrows(quiver):
    for arrow in quiver:
        if (arrow.get('range') is True or None) or not arrow.get('damaged'):
            return True
    return False
