def alphabet_war(fight):
    l_letters = {'w': 4, 'p': 3, 'b': 2, 's': 1}
    r_letters = {'m': 4, 'q': 3, 'd': 2, 'z': 1}
    l_sum = 0
    r_sum = 0
    for letter in fight:
        for (key, value) in l_letters.items():
            if key == letter:
                l_sum += value
        for (key, value) in r_letters.items():
            if key == letter:
                r_sum += value
    if r_sum > l_sum:
        return 'Right side wins!'
    elif r_sum < l_sum:
        return 'Left side wins!'
    else:
        return "Let's fight again!"
