def any_arrows(arrows):
    if arrows == []:
        return False
    else:
        for i in arrows:
            if not 'damaged' in i:
                return True
            elif i['damaged']==False:
                return True
        return False
