def any_arrows(arrows):
    if arrows == []:
        return False
    for dictionary in arrows:
        if 'damaged' not in dictionary:
            return True
        if 'damaged' in dictionary:
            if dictionary['damaged'] == False:
                return True
    return False
