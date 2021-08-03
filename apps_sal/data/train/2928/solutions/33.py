def alphabet_war(fight):
    left_power = {'w': 4, 'p': 3, 'b': 2, 's': 1}
    right_power = {'m': 4, 'q': 3, 'd': 2, 'z': 1}

    left_sum = 0
    right_sum = 0

    for char in fight:
        if char in left_power:
            left_sum += left_power[char]
        elif char in right_power:
            right_sum += right_power[char]

    if left_sum > right_sum:
        return "Left side wins!"
    elif left_sum < right_sum:
        return "Right side wins!"
    else:
        return "Let's fight again!"
