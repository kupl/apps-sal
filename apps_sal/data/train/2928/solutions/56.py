def alphabet_war(fight):
    s = 0
    for c in fight:
        if c in 'mqdzsbpw':
            s += 'mqdz_sbpw'.index(c) - 4
    if s > 0:
        return 'Left side wins!'
    elif s == 0:
        return "Let's fight again!"
    else:
        return 'Right side wins!'
