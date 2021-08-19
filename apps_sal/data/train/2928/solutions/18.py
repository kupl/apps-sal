def alphabet_war(fight):
    left = {'w': 4, 'p': 3, 'b': 2, 's': 1}
    right = {'m': 4, 'q': 3, 'd': 2, 'z': 1}
    sl = 0
    rl = 0
    for letter in fight:
        if letter in left.keys():
            sl += left[letter]
        elif letter in right.keys():
            rl += right[letter]
    if sl > rl:
        return 'Left side wins!'
    elif rl > sl:
        return 'Right side wins!'
    else:
        return "Let's fight again!"
