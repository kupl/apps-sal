def areYouPlayingBanjo(name):
    play = False
    if name != '' and name[0] in ('r', 'R'):
        play = True

    res = name + ' does not play banjo'
    if (play == True):
        res = name + ' plays banjo'
    return res
