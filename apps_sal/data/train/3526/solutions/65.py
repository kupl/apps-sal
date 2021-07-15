def any_arrows(arrows):
    status = False
    for arrow in arrows:
        if not arrow.get('damaged', False):
            status = True
    return status

