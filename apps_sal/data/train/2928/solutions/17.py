def alphabet_war(fight):
    left_side = {"w": 4, "p": 3, "b": 2, "s": 1}
    right_side = {"m": 4, "q": 3, "d": 2, "z": 1}
    left_points = 0
    right_points = 0
    for l in fight:
        if l in left_side:
            left_points += left_side[l]
        elif l in right_side:
            right_points += right_side[l]
    if left_points > right_points:
        return "Left side wins!"
    elif left_points < right_points:
        return "Right side wins!"
    else:
        return "Let's fight again!"
