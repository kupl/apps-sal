def alphabet_war(fight):
    powers = {'w': 4, 'p': 3, 'b': 2, 's': 1, 'm': -4, 'q': -3, 'd': -2, 'z': -1}
    sum = 0
    for char in fight:
        for letter in powers:
            if char == letter:
                sum += powers[letter]
    if sum > 0:
        return 'Left side wins!'
    elif sum < 0:
        return 'Right side wins!'
    else:
        return "Let's fight again!"
