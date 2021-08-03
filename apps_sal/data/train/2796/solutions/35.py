def areYouPlayingBanjo(name):
    return name + (name[0] in "Rr") * " plays banjo" + (name[0] not in "Rr") * (" does not play banjo")
