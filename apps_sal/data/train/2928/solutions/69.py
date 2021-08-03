def alphabet_war(fight):
    left = {"w": 4, "p": 3, "b": 2, "s": 1}
    right = {"m": 4, "q": 3, "d": 2, "z": 1}
    l, r = 0, 0
    for i in fight:
        if i in left:
            l += left[i]
        if i in right:
            r += right[i]
    if l > r:
        return 'Left side wins!'
    if r > l:
        return 'Right side wins!'
    return "Let's fight again!"
