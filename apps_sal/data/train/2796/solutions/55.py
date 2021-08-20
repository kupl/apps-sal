def areYouPlayingBanjo(name):
    x = name.title()
    if x[0] == 'R':
        return name + ' plays banjo'
    else:
        return name + ' does not play banjo'
