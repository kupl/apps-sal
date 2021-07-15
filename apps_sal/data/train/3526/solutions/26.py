def any_arrows(arrows):
    if arrows == []:
        return False
    else:
        for i in arrows:
            if i.get("damaged") is None:
                return True
                break
            elif i["damaged"] == False:
                return True
                break
        else:
            return False

