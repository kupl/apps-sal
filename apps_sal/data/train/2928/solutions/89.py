def alphabet_war(fight):
    left = {'w': 4, 'p': 3, 'b': 2, 's': 1}
    right = {'m': 4, 'q': 3, 'd': 2, 'z': 1}
    left_total = 0
    right_total = 0
    for letter in fight:
        if letter in left:
            left_total += left[letter]
        if letter in right:
            right_total += right[letter]
    if left_total > right_total:
        return 'Left side wins!'
    elif left_total < right_total:
        return 'Right side wins!'
    else:
        return "Let's fight again!"
