def any_arrows(arrows):
    # print(arrows)
    return any(not arrow.get('damaged', False) for arrow in arrows)
