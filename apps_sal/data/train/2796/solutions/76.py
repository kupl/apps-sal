def areYouPlayingBanjo(name):
    first = name[0]
    if first == 'R':
        return name + ' ' + 'plays banjo'
    elif first == 'r':
        return name + ' ' + 'plays banjo'
    else:
        return name + ' ' + 'does not play banjo'


print(areYouPlayingBanjo('Martin'))
