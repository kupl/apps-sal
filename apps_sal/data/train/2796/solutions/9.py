def areYouPlayingBanjo(name):
    if name[0].lower() == 'r':
        return '{} plays banjo'.format(name)
    else:
        return '{} does not play banjo'.format(name)
