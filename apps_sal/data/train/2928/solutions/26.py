def alphabet_war(fight):
    ls = ['s', 'b', 'p', 'w', 'z', 'd', 'q', 'm']
    a, b = 0, 0
    for i in list(fight):
        if i in ls:
            if ls.index(i) > 3:
                a += ls.index(i) - 3
            else:
                b += ls.index(i) + 1
    return "Let's fight again!" if a == b else "Right side wins!" if a > b else "Left side wins!"
