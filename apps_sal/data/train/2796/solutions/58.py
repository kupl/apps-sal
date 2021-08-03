def areYouPlayingBanjo(name):
    for i in name:
        if i[0] == ("r") or i[0] == ("R"):
            return name + " plays banjo"
        else:
            return name + " does not play banjo"
