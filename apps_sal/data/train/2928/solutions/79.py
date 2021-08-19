def alphabet_war(fight):
    powers = {'w': 4, 'p': 3, 'b': 2, 's': 1, 'm': -4, 'q': -3, 'd': -2, 'z': -1}
    points = sum((powers.get(f, 0) for f in fight))
    if points > 0:
        return 'Left side wins!'
    elif points == 0:
        return "Let's fight again!"
    return 'Right side wins!'
