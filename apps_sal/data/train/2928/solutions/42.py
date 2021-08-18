def alphabet_war(fight):
    left_score = 0
    right_score = 0
    for l in list(fight):
        if l == "w":
            left_score += 4
        elif l == "p":
            left_score += 3
        elif l == "b":
            left_score += 2
        elif l == "s":
            left_score += 1
        elif l == "m":
            right_score += 4
        elif l == "q":
            right_score += 3
        elif l == "d":
            right_score += 2
        elif l == "z":
            right_score += 1
    if left_score > right_score:
        return "Left side wins!"
    elif left_score < right_score:
        return "Right side wins!"
    elif right_score == left_score:
        return "Let's fight again!"
