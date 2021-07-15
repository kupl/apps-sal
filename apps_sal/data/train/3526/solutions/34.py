def any_arrows(arrows):
    lst = []
    
    if arrows == []:
        lst.append(False)
    else:
        for arrow in arrows:
            if 'damaged' not in arrow.keys():
                lst.append(True)
            elif 'damaged' in arrow.keys() and arrow['damaged'] == False:
                lst.append(True)
            else:
                lst.append(False)
    return True in lst
