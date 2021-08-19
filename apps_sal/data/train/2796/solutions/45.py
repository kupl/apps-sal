def areYouPlayingBanjo(name):
    banjo = ('R', 'r')
    if name[0] in banjo:
        return name + ' plays banjo'
    else:
        return name + ' does not play banjo'
