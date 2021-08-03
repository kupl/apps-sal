def alphabet_war(fight):
    if fight == '':
        return "Let's fight again!"
    left_side = {'s': 1, 'b': 2, 'p': 3, 'w': 4}
    right_side = {'z': 1, 'd': 2, 'q': 3, 'm': 4}
    left_side_count = 0
    right_side_count = 0
    for letter in fight:
        if letter in left_side:
            left_side_count += left_side[letter]
        elif letter in right_side:
            right_side_count += right_side[letter]
    if left_side_count > right_side_count:
        answer = 'Left side wins!'
    elif right_side_count > left_side_count:
        answer = 'Right side wins!'
    else:
        answer = "Let's fight again!"
    return answer
