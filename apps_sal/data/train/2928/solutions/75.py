def alphabet_war(fight):
    left = 0
    right = 0
    for i in fight:
        if i in 'w':
            left += 4
        elif i in 'p':
            left += 3
        elif i in 'b':
            left += 2
        elif i in 's':
            left += 1
        elif i in 'm':
            right += 4
        elif i in 'q':
            right += 3
        elif i in 'd':
            right += 2
        elif i in 'z':
            right += 1
    if right > left:
        return 'Right side wins!'
    if left > right:
        return 'Left side wins!'
    else:
        return "Let's fight again!"
