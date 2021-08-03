def any_arrows(arrows):
    if arrows == []:
        return False
    else:
        for i in range(len(arrows)):
            if arrows[i].get('damaged') == False or arrows[i].get('damaged') == None:
                return True
                break
        return False
