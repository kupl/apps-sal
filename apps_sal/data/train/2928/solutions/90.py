def alphabet_war(fight):
    left_scores = {'w': 4, 'p': 3, 'b': 2, 's': 1}
    right_scores = {'m': 4, 'q': 3, 'd': 2, 'z': 1}
    left_score = 0
    right_score = 0
    for char in fight:
        if char in left_scores.keys():
            left_score += left_scores[char]
        elif char in right_scores.keys():
            right_score += right_scores[char]
    if right_score > left_score:
        return 'Right side wins!'
    elif left_score > right_score:
        return 'Left side wins!'
    else:
        return "Let's fight again!"
