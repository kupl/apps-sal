def areYouPlayingBanjo(name):
    return name + [' does not play', ' plays'][name[0].startswith(('R', 'r'))] + ' banjo'
