def areYouPlayingBanjo(name):
    output = ''
    if name.lower()[0] == 'r':
        output = ' plays banjo'
    else:
        output = ' does not play banjo'
    return name + output
