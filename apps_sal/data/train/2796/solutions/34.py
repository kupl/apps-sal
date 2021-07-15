def areYouPlayingBanjo(name):
    # name = name.title()
    # if name.startswith('R'):
    #     return name + " plays banjo"
    # else:
    #     return name + " does not play banjo"
    return name + (" plays" if name.title().startswith('R') else " does not play") + " banjo"
