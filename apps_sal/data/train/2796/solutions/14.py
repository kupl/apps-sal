def areYouPlayingBanjo(name):
    if name[0] in 'rR':
        return '{name} plays banjo'.format(name=name)
    else:
        return '{name} does not play banjo'.format(name=name)
