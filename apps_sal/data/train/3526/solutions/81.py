def any_arrows(arrows):
    return any([i.get('damaged',False) == False for i in arrows]) if arrows else False
            

