def areYouPlayingBanjo(name):
    return '{} {} banjo'.format(name, ['does not play', 'plays'][name[0] in 'Rr'])
