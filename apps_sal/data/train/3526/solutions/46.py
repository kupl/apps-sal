def any_arrows(arrows):
    count=0
    for i in arrows:
        try:
            if not i['damaged']:
                return True
        except:
            return True
    return False
