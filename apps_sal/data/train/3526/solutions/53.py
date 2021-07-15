def any_arrows(arrows):
    for arrow in arrows:
        try : 
            if arrow['damaged'] == False : return True
        except : return True
    return False
