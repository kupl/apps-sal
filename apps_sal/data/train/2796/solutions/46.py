def areYouPlayingBanjo(name):
    if name.lower()[0] == 'r':
        banjo = name + " plays banjo"
    else:
        banjo = name + " does not play banjo"
    return banjo
