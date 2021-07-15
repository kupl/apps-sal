def any_arrows(arrows):
    if len(arrows) == 0:
        return False
    else:
        for arrow_info in arrows:
            if arrow_info.get('damaged') == None:
                return True
            elif arrow_info.get('damaged') == False:
                return True
        return False
