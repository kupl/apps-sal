def alphabet_war(fight):
    left = ['w', 'p', 'b', 's']
    right = ['m', 'q', 'd', 'z']

    powers = {'w': 4, 'p': 3, 'b': 2, 's': 1, 'm': 4, 'q': 3, 'd': 2, 'z': 1}

    phrase = list(fight)
    left_total = 0
    right_total = 0

    for letter in phrase:
        if letter in right:
            right_total = right_total + powers[letter]
        if letter in left:
            left_total = left_total + powers[letter]

    if left_total > right_total:
        return "Left side wins!"
    if right_total > left_total:
        return "Right side wins!"

    return "Let's fight again!"
