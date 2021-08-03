def areYouPlayingBanjo(name):
    first_letter = list(name)[0].lower()
    if first_letter == 'r':
        return(name + " plays banjo")
    return(name + " does not play banjo")
