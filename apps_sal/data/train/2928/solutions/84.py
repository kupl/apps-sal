def alphabet_war(fight):
    # your code here
    left = {'w': -4, 'p': -3, 'b': -2, 's': -1}
    right = {'m': 4, 'q': 3, 'd': 2, 'z': 1}
    left.update(right)
    points = sum([left[x] for x in fight if x in left])
    win = 'Left side wins!' if points < 0 else "Let's fight again!" if points == 0 else 'Right side wins!'
    return(win)
