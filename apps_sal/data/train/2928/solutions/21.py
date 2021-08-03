LEFT = 'wpbs'[::-1]
RIGHT = 'mqdz'[::-1]


def points(s, dictionary):
    return sum([dictionary.find(e) + 1 for e in s])


def alphabet_war(fight):
    left, right = points(fight, LEFT), points(fight, RIGHT)

    if left > right:
        return 'Left side wins!'
    elif right > left:
        return 'Right side wins!'
    else:
        return "Let's fight again!"
