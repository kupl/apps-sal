def alphabet_war(fight):
    (r, l) = (0, 0)
    c = 1
    for i in 'sbpw':
        l += fight.count(i) * c
        c += 1
    c = 1
    for i in 'zdqm':
        r += fight.count(i) * c
        c += 1
    if l > r:
        return 'Left side wins!'
    elif r > l:
        return 'Right side wins!'
    else:
        return "Let's fight again!"
