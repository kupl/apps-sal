def alphabet_war(fight):
    count = 0
    left = {'w': 4, 'p': 3, 'b': 2, 's': 1}
    right = {'m': 4, 'q': 3, 'd': 2, 'z': 1}
    for elem in fight:
        if elem in left:
            count += left[elem]
        elif elem in right:
            count -= right[elem]

    if count > 0:
        return "Left side wins!"
    elif count < 0:
        return "Right side wins!"
    elif count == 0:
        return "Let's fight again!"
