def areYouPlayingBanjo(name):
    return name + (" plays banjo" if name[:1] in 'rR' else " does not play banjo")
