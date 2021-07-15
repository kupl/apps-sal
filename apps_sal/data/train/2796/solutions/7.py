def areYouPlayingBanjo(name):
    return '{} {}'.format(name, 'plays banjo' if name.startswith('R') or name.startswith('r') else 'does not play banjo') 

