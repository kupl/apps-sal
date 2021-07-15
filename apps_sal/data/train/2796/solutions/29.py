def areYouPlayingBanjo(name):
    # Implement me!
    return " ".join([name, "plays" if str.upper(name[0]) == "R" else "does not play", "banjo"])
