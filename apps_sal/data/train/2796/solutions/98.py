def areYouPlayingBanjo(name):
    if list(name)[0] == 'R' or list(name)[0] == 'r':
        return f'{name} plays banjo'
    else:
        return f'{name} does not play banjo'
