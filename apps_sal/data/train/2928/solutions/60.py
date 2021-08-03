d = {'w': -4, 'p': -3, 'b': -2, 's': -1,
     'm': 4, 'q': 3, 'd': 2, 'z': 1}


def alphabet_war(s):
    f = sum(d[l] if l in d else 0 for l in s)
    return (f > 0) * 'Right side wins!' + (f == 0) * 'Let\'s fight again!' + (f < 0) * 'Left side wins!'
