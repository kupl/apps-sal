def any_arrows(arrows):
    if not arrows:
        status = False
    for arrow in arrows:
        if 'damaged' not in arrow or arrow['damaged'] == False:
            status = True
            break
        else:
            status = False
    return status
