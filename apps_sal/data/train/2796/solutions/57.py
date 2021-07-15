def areYouPlayingBanjo(n):
    if n[0].lower() == 'r':
        result = 'plays'
    else:
        result = 'does not play'
    return f'{n} {result} banjo'
