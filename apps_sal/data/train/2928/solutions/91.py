def alphabet_war(fight):
    powersLeft = {'w': 4, 'p': 3, 'b': 2, 's': 1}
    powersRight = {'m': 4, 'q': 3, 'd': 2, 'z': 1}
    left = 0
    right = 0
    for letter in fight:
        if letter in powersLeft:
            left += powersLeft[letter]
        elif letter in powersRight:
            right += powersRight[letter]
    if left > right:
        return 'Left side wins!'
    elif left < right:
        return 'Right side wins!'
    return 'Let\'s fight again!'
