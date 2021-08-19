def areYouPlayingBanjo(name):
    return '{} {} banjo'.format(name, 'plays' if name.lower().startswith('r') else 'does not play')
