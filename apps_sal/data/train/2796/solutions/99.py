def areYouPlayingBanjo(name):
    if name.casefold().startswith("r"):
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"
