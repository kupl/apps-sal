def any_arrows(arrows):
    has_good = False
    for arrow in arrows:
        is_damaged = arrow.get('damaged', False)
        if not is_damaged:
            has_good = True
            break
    return has_good
