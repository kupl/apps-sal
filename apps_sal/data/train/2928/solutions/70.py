def alphabet_war(fight):
    power = 0
    left = {'w': 4, 'p': 3, 'b': 2, 's': 1}
    right = {'m': 4, 'q': 3, 'd': 2, 'z': 1}
    for i in fight:
        if i in left:
            power += left[i]
        elif i in right:
            power -= right[i]
    if power < 0:
        return "Right side wins!"
    if power > 0:
        return "Left side wins!"
    elif power == 0:
        return "Let's fight again!"
