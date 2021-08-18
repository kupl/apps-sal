def areYouPlayingBanjo(name):

    nametolist = list(name)

    if nametolist[0] == 'R':
        return name + " plays banjo"
    elif nametolist[0] == 'r':
        return name + " plays banjo"
    else:
        return name + " does not play banjo"
