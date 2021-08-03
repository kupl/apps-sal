def alphabet_war(f):
    p = {'w': -4, 'p': -3, 'b': -2, 's': -1, 'm': 4, 'q': 3, 'd': 2, 'z': 1}
    if sum(p[x] for x in f if x in p) == 0:
        return "Let's fight again!"

    return "Right side wins!" if sum(p[x] for x in f if x in p) > 0 else "Left side wins!"
