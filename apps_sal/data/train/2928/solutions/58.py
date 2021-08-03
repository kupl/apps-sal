def alphabet_war(fight):
    left = {'w': 4, 'p': 3, 'b': 2, 's': 1}
    right = {'m': 4, 'q': 3, 'd': 2, 'z': 1}

    L = sum([left.get(i, 0) for i in fight])
    R = sum([right.get(i, 0) for i in fight])

    if L > R:
        return 'Left side wins!'
    elif L < R:
        return 'Right side wins!'
    else:
        return "Let's fight again!"
