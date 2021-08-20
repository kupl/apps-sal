def areYouPlayingBanjo(name):
    list = []
    for i in name:
        list.append(i)
    if list[0] == 'R':
        return name + ' plays banjo'
    elif list[0] == 'r':
        return name + ' plays banjo'
    elif list[0] != 'R':
        return name + ' does not play banjo'
    elif list[0] != 'r':
        return name + ' does not play banjo'
    else:
        return 'please try again michelle'
