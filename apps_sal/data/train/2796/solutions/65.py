def areYouPlayingBanjo(name):
    return f'{name} plays banjo' if name.startswith('r') or name[0] == 'R' else f'{name} does not play banjo'
