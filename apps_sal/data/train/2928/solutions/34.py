def alphabet_war(fight):
    dic1_left = {'w': 4, 'p': 3, 'b': 2, 's': 1}
    left_score = 0
    dic2_right = {'m': 4, 'q': 3, 'd': 2, 'z': 1}
    right_score = 0
    no_score = 0
    for i in fight:
        if i in dic1_left:
            left_score += dic1_left[i]
        elif i in dic2_right:
            right_score += dic2_right[i]
        else:
            no_score += 0
    if left_score > right_score:
        return 'Left side wins!'
    elif left_score == right_score:
        return "Let's fight again!"
    else:
        return 'Right side wins!'
