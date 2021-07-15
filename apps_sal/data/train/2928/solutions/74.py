def alphabet_war(fight):
    right = 0
    left = 0
    for letters in fight:
        if letters == 'w':
            left += 4
        elif letters == 'p':
            left +=3
        elif letters == 'b':
            left += 2
        elif letters == 's':
            left += 1
        elif letters == 'm':
            right += 4
        elif letters == 'q':
            right += 3
        elif letters == 'd':
            right += 2
        elif letters == 'z':
            right += 1
        else:
            pass
    if right > left:
        return "Right side wins!"
    elif right < left:
        return "Left side wins!"
    else:
        return "Let's fight again!"
