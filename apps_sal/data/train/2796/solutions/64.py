def areYouPlayingBanjo(name):
    plays = ' does not play banjo'
    if name[0].lower() == 'r':
        plays = ' plays banjo'
    return name + plays
