def areYouPlayingBanjo(name):
    return (f'{name} does not play banjo', f'{name} plays banjo')[name[0].lower() == 'r']
