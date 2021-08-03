def areYouPlayingBanjo(name):
    first_letter = name[0]
    print(first_letter)
    if first_letter == "R" or first_letter == "r":
        return name + " plays banjo"
    return name + " does not play banjo"
