def areYouPlayingBanjo(name):
    # Implement me!
    if name.upper()[0] == "R":
        text = "{} plays banjo".format(name)
    else:
        text = "{} does not play banjo".format(name)
    return text
