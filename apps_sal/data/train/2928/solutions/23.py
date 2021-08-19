def alphabet_war(fight):
    leftSide = {'w': 4, 'p': 3, 'b': 2, 's': 1}
    rightSide = {'m': 4, 'q': 3, 'd': 2, 'z': 1}
    left = []
    right = []
    for letter in fight:
        left.append(leftSide.get(letter, 0))
        right.append(rightSide.get(letter, 0))
    if sum(left) == sum(right):
        return "Let's fight again!"
    elif sum(left) > sum(right):
        return 'Left side wins!'
    elif sum(left) < sum(right):
        return 'Right side wins!'
