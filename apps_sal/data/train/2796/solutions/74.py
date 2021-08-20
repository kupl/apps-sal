def areYouPlayingBanjo(name):
    result = ' plays banjo' if name.lower()[0] == 'r' else ' does not play banjo'
    return name + result
