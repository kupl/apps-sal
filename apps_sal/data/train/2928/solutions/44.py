def alphabet_war(fight):
    left = 0
    right = 0
    for i in fight:
        if i == 'w':
            left += 4
        if i == 'p':
            left += 3
        if i == 'b':
            left += 2
        if i == 's':
            left += 1
        if i == 'm':
            right += 4
        if i == 'q':
            right += 3
        if i == 'd':
            right += 2
        if i == 'z':
            right += 1
    if left > right:
        return 'Left side wins!'
    elif right > left:
        return 'Right side wins!'
    else:
        return "Let's fight again!"
