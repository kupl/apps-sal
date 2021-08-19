def areYouPlayingBanjo(name):
    i = name[0:1]
    if i == 'R' or i == 'r':
        return f'{name} plays banjo'
    else:
        return f'{name} does not play banjo'
