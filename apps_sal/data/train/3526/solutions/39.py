def any_arrows(arrows):
    if not arrows:
        return False
    for d in arrows:
        if any((d[k] == False for k in d)) or 'damaged' not in d.keys():
            return True
    return False
