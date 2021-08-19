def alphabet_war(fight):
    left_alp = {'w': 4, 'p': 3, 'b': 2, 's': 1}
    right_alp = {'m': 4, 'q': 3, 'd': 2, 'z': 1}
    left_score = 0
    right_score = 0
    for i in left_alp:
        left_score += fight.count(i) * left_alp[i]
    for i in right_alp:
        right_score += fight.count(i) * right_alp[i]
    return 'Right side wins!' if right_score > left_score else "Let's fight again!" if right_score == left_score else 'Left side wins!'
