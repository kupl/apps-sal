def areYouPlayingBanjo(name):

    nametolist = list(name)    # Converting the string to a list

    if nametolist[0] == 'R':    # Testing if first character is an 'R'
        return name + " plays banjo"
    elif nametolist[0] == 'r':
        return name + " plays banjo"
    else:
        return name + " does not play banjo"
