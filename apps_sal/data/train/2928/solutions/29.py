def alphabet_war(fight):
    d = {'w': 4, 'p': 3, 'b': 2, 's': 1, 'm': -4, 'q': -3, 'd': -2, 'z': -1}
    result = sum(d[c] for c in fight if c in d)
    return 'Left side wins!' if result > 0 else ('Right side wins!' if result < 0 else 'Let\'s fight again!')
