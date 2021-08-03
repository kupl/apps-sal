print("Are you playing banjo?")


def areYouPlayingBanjo(name):
    # return positive if name.lower().startswith "r"
    if name.lower().startswith("r"):
        return name + " plays banjo"
    else:
        return name + " does not play banjo"
    return name


areYouPlayingBanjo("martin")
areYouPlayingBanjo("Rikke")
