def alphabet_war(fight):
    lres = 0
    rres = 0
    ldicc = {'w': 4, 'p': 3, 'b': 2, 's': 1}
    rdicc = {'m': 4, 'q': 3, 'd': 2, 'z': 1}
    for elem in fight:
        if elem in ldicc:
            lres = lres + ldicc[elem]
        elif elem in rdicc:
            rres = rres + rdicc[elem]
    if rres > lres:
        return 'Right side wins!'
    elif lres > rres:
        return 'Left side wins!'
    else:
        return "Let's fight again!"
