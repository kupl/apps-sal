def alphabet_war(fight):
    # your code here
    left = {'w': 4, 'p': 3, 'b': 2, 's': 1}
    right = {'m': 4, 'q': 3, 'd': 2, 'z': 1}

    l = 0
    r = 0

    for letter in fight:
        if letter in left:
            l += left[letter]
        elif letter in right:
            r += right[letter]

    if l > r:
        return 'Left side wins!'
    elif r > l:
        return 'Right side wins!'
    else:
        return 'Let\'s fight again!'
