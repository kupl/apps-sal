def areYouPlayingBanjo(name):
    result = ''
    if name[0] == 'r' or name[0] == 'R':
        result += ' plays banjo'
    else:
        result += ' does not play banjo'
    return name + result
