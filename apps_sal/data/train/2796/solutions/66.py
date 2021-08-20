def areYouPlayingBanjo(name):
    condition = 'plays' if name[0].lower() == 'r' else 'does not play'
    return f'{name} {condition} banjo'
