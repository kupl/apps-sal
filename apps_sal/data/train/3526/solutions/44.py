def any_arrows(arrows):
    for arrow in arrows:
        if "damaged" not in arrow.keys():
            return True
        elif arrow["damaged"] == False:
            return True
    else: return False
