def alphabet_war(fight):
    r, r_c = 'zdqm', 0
    l, l_c = 'sbpw', 0
    for i in fight:
        if i in r:
            r_c += r.index(i) + 1
        elif i in l:
            l_c += l.index(i) + 1
    if r_c > l_c:
        return 'Right side wins!'
    elif l_c > r_c:
        return 'Left side wins!'
    else:
        return "Let's fight again!"
