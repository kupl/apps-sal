def areYouPlayingBanjo(name):
    return "%s %s banjo" % (name, ["does not play", "plays"][name[0].lower() == 'r'])
