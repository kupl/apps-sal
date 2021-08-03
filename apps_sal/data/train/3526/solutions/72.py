def any_arrows(arrows):
    res = []
    for i in range(len(arrows)):
        if 'damaged' in list(arrows[i].keys()):
            if arrows[i]['damaged'] == True:
                res.append(True)
            else:
                res.append(False)
        else:
            res.append(False)
    return False in res
