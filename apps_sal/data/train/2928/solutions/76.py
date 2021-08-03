def alphabet_war(fight, n=0):
    alpha = {'s': 1, 'z': -1, 'b': 2, 'd': -2, 'p': 3, 'q': -3, 'w': 4, 'm': -4}

    for c in fight:
        n += alpha.get(c, 0)

    return ("Left" if n > 0 else "Right") + " side wins!" if n else "Let's fight again!"
