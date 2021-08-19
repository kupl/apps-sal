def areYouPlayingBanjo(name):
    if name.startswith(('R', 'r')):
        return '{} plays banjo'.format(name)
    return '{} does not play banjo'.format(name)
