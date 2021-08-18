print("Are you playing banjo?")


def areYouPlayingBanjo(name):
    if name.lower().startswith("r"):
        return name + " plays banjo"
    else:
        return name + " does not play banjo"
    return name


areYouPlayingBanjo("martin")
areYouPlayingBanjo("Rikke")
