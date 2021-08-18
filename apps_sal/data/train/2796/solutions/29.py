def areYouPlayingBanjo(name):
    return " ".join([name, "plays" if str.upper(name[0]) == "R" else "does not play", "banjo"])
