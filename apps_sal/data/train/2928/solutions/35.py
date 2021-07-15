def alphabet_war(fight):
    score = 0
    for i in fight:
        if i == 'w':
            score += 4
        elif i == 'p':
            score += 3
        elif i == 'b':
            score += 2
        elif i == 's':
            score += 1
        elif i == 'm':
            score -= 4
        elif i == 'q':
            score -= 3
        elif i == 'd':
            score -= 2
        elif i == 'z':
            score -= 1
    if score > 0:
        return "Left side wins!"
    elif score < 0:
        return "Right side wins!"
    else:
        return "Let's fight again!"
