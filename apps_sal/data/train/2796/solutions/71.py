def areYouPlayingBanjo(name):
    plays = 'does not play' if name[0] not in 'Rr' else 'plays'
    return f'{name} {plays} banjo'
