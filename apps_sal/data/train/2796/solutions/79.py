def areYouPlayingBanjo(name):
    checkname = name.lower()
    if checkname.startswith('r'):
        return name + ' plays banjo'
    else:
        return name + ' does not play banjo'
