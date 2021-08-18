def any_arrows(arrows):
    i = 0
    while i < len(arrows):
        if not arrows[i].get("damaged"):
            return True
        i = i + 1
    return False
