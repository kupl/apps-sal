def areYouPlayingBanjo(name):
    b=' plays banjo'
    nb=' does not play banjo'
    if name[0].lower()== 'r':
        name = name + b
        return name
    else:
        name = name + nb
        return name
