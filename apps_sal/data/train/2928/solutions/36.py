def alphabet_war(fight):
    left = {
        "w": 4,
        "p": 3,
        "b": 2,
        "s": 1
    }
    right = {
        "m": 4,
        'q': 3,
        'd': 2,
        'z': 1
    }
    l = sum(left[i] for i in fight if i in left)
    r = sum(right[i] for i in fight if i in right)
    if l > r:
        return "Left side wins!"
    if r > l:
        return "Right side wins!"
    return "Let's fight again!"
