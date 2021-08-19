def any_arrows(arrows):
    if arrows:
        for d in arrows:
            if not 'damaged' in d:
                return True
            elif not d['damaged']:
                return True
    return False
