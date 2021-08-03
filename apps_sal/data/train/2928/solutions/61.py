d1 = {
    "w": 4,
    "p": 3,
    "b": 2,
    "s": 1
}
d2 = {
    "m": 4,
    "q": 3,
    "d": 2,
    "z": 1
}


def alphabet_war(fight):
    r = 0
    l = 0
    for i in fight:
        if i in d1.keys():
            l += d1[i]
        elif i in d2.keys():
            r += d2[i]

    return 'Right side wins!' if r > l else 'Left side wins!' if l > r else "Let's fight again!"
