def alphabet_war(fight):
    left_side = {'w': 4, 'p': 3, 'b': 2, 's': 1}
    right_side = {'m': 4, 'q': 3, 'd': 2, 'z': 1}
    left_side_total = 0
    right_side_total = 0
    for eachletter in fight:
        if eachletter in left_side.keys():
            left_side_total = left_side_total + left_side[eachletter]
        elif eachletter in right_side.keys():
            right_side_total = right_side_total + right_side[eachletter]
    if left_side_total > right_side_total:
        return 'Left side wins!'
    elif right_side_total > left_side_total:
        return 'Right side wins!'
    else:
        return 'Let\'s fight again!'
