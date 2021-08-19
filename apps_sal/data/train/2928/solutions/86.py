db = {'w': 4, 'p': 3, 'b': 2, 's': 1, 'm': 4, 'q': 3, 'd': 2, 'z': 1}


def alphabet_war(fight):
    l = r = 0
    for i in fight:
        if i in 'wpbs':
            l += db[i]
        elif i in 'mqdz':
            r += db[i]
    return 'Left side wins!' if l > r else 'Right side wins!' if r > l else "Let's fight again!"
