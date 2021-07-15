def areYouPlayingBanjo(name):
    return '{} {}'.format(name, ['does not play banjo', 'plays banjo'][name[0] in 'rR'])
