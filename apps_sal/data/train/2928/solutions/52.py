d = {'w': 4, 'p': 3, 'b': 2, 's': 1, 'm': -4, 'q': -3, 'd': -2, 'z': -1}
def alphabet_war(fight):
    s = sum(d.get(c, 0) for c in fight)
    return 'Left side wins!' if s>0 else 'Right side wins!' if s<0 else 'Let\'s fight again!'
