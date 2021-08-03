def alphabet_war(fight):
    rules = {
        'w': 4,
        'p': 3,
        'b': 2,
        's': 1,
        'm': -4,
        'q': -3,
        'd': -2,
        'z': -1
    }
    fight = list([i for i in [x for x in fight] if i in 'wpbsmqdz'])
    res = sum([rules.get(x) for x in fight])
    if res == 0:
        return "Let's fight again!"
    return "Right side wins!" if res < 0 else "Left side wins!"
