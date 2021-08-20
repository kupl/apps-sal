def any_arrows(arrows):
    for item in arrows:
        try:
            a = item['damaged']
            if not a:
                return True
        except:
            return True
    return False
