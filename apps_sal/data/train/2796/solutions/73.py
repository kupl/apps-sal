def areYouPlayingBanjo(name):
    a = name + ' plays banjo'
    b = name + ' does not play banjo'
    if name[0] == 'r' or name[0] == 'R':
        return a
    else:
        return b
