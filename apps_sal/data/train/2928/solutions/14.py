def alphabet_war(fight):
    left_letters = {"w": 4, "p": 3, "b": 2, "s": 1}
    right_letters = {"m": 4, "q": 3, "d": 2, "z": 1}

    count_left = []
    count_right = []

    fight = list(map(str, fight))

    for e in fight:
        for key, value in list(left_letters.items()):
            if e == key:
                count_left.append(value)

    for e in fight:
        for key, value in list(right_letters.items()):
            if e == key:
                count_right.append(value)

    total_left = sum(count_left)
    total_right = sum(count_right)

    if total_left > total_right:
        return "Left side wins!"
    elif total_left < total_right:
        return "Right side wins!"
    else:
        return "Let's fight again!"
