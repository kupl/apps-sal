def areYouPlayingBanjo(name):
    lst = list(name)
    if lst[0] == 'r' or lst[0] == 'R':
        return f'{name} plays banjo'
    else:
        return f'{name} does not play banjo'
