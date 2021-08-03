def areYouPlayingBanjo(name):
    check = any(x is name[0] for x in "rR")
    return f"{name} plays banjo" if check else f"{name} does not play banjo"
