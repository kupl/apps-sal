def alphabet_war(fight):
    left_side = {'w': 4, 'p': 3, 'b': 2, 's': 1}
    right_side = {'m': 4, 'q': 3, 'd': 2, 'z': 1}
    total = 0
    for char in fight:
        if char in list(left_side.keys()):
            total += left_side[char]
        elif char in list(right_side.keys()):
            total -= right_side[char]
        else:
            total += 0

    if total > 0:
        return "Left side wins!"
    elif total < 0:
        return "Right side wins!"
    else:
        return "Let's fight again!"
