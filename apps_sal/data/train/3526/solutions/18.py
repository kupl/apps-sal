def any_arrows(arrows):
    return True if ['undamaged' for i in arrows if not i.get('damaged')] else False
