def alphabet_war(fight):
    left_power = 0
    right_power = 0
    fight = list(fight)
    for letter in fight:
        if letter == "z":
            right_power += 1
        elif letter == "d":
            right_power += 2
        elif letter == "q":
            right_power += 3
        elif letter == "m":
            right_power += 4
        elif letter == "s":
            left_power += 1
        elif letter == "b":
            left_power += 2
        elif letter == "p":
            left_power += 3
        elif letter == "w":
            left_power += 4
        else:
            continue

    if left_power > right_power:
        return "Left side wins!"
    elif right_power > left_power:
        return "Right side wins!"
    elif right_power == left_power:
        return "Let's fight again!"
