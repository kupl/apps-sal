def areYouPlayingBanjo(name):
    return "{} plays banjo".format(name) if name[0] in "Rr" else "{} does not play banjo".format(name)
