def alphabet_war(fight):
    left_side = {"w": 4, "p": 3, "b": 2, "s": 1}
    right_side = {"m": 4, "q": 3, "d": 2, "z": 1}
    left_points = sum([left_side[l] for l in fight if l in left_side])
    right_points = sum([right_side[l] for l in fight if l in right_side])
    if left_points > right_points:
        return "Left side wins!"
    elif left_points < right_points:
        return "Right side wins!"
    else:
        return "Let's fight again!"
