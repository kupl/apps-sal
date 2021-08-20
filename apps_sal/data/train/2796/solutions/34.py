def areYouPlayingBanjo(name):
    return name + (' plays' if name.title().startswith('R') else ' does not play') + ' banjo'
