def alphabet_war(fight):
    right = {'m': 4, 'q': 3, 'd': 2, 'z': 1}
    left = {'w':4, 'p': 3, 'b': 2, 's': 1}
    rarr = []
    larr = []
    for s in fight:
        if s in 'mqdz':
            rarr.append(right.get(s))
        elif s in 'wpbs':
            larr.append(left.get(s))
    return 'Left side wins!' if sum(larr) > sum(rarr) else 'Right side wins!' if sum(rarr) > sum(larr) else 'Let\'s fight again!'


