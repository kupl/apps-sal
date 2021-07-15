def any_arrows(arrows):
    if arrows==[]:
        return False 
    for i in arrows:
        if i.get('damaged', 0)==False:
            return True
    return False

