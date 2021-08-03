def alphabet_war(fight):
    left_score = 0
    right_score = 0
    left_char = ['w', 'p', 'b', 's']
    right_char = ['m', 'q', 'd', 'z']
    for char in fight:
        if char in left_char:
            if char == left_char[0]:
                left_score += 4
            elif char == left_char[1]:
                left_score += 3
            elif char == left_char[2]:
                left_score += 2
            elif char == left_char[3]:
                left_score += 1
        elif char in right_char:
            if char == right_char[0]:
                right_score += 4
            elif char == right_char[1]:
                right_score += 3
            elif char == right_char[2]:
                right_score += 2
            elif char == right_char[3]:
                right_score += 1
    if left_score > right_score:
        return 'Left side wins!'
    elif left_score < right_score:
        return 'Right side wins!'
    elif left_score == right_score:
        return "Let's fight again!"
