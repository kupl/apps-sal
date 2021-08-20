def alphabet_war(fight):
    left_letters = {'w': 4, 'p': 3, 'b': 2, 's': 1}
    right_letters = {'m': 4, 'q': 3, 'd': 2, 'z': 1}
    sum_left = 0
    sum_right = 0
    fight = fight.lower()
    for char in fight:
        if char in left_letters:
            number1 = left_letters[char]
            sum_left += number1
        elif char in right_letters:
            number2 = right_letters[char]
            sum_right += number2
    if sum_left > sum_right:
        return 'Left side wins!'
    elif sum_right > sum_left:
        return 'Right side wins!'
    else:
        return "Let's fight again!"
