def alphabet_war(fight):
    left = {'w': 4, 'p': 3, 'b': 2, 's': 1}
    right = {'m': 4, 'q': 3, 'd': 2, 'z': 1}
    left_score = sum([left[i] for i in fight if i in left])
    right_score = sum([right[i] for i in fight if i in right])
    if left_score > right_score:
        return "Left side wins!"
    elif left_score < right_score:
        return "Right side wins!"
    else:
        return "Let's fight again!"
