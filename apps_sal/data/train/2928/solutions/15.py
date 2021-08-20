def alphabet_war(fight):
    left_points = sum([{'w': 4, 'p': 3, 'b': 2, 's': 1}[l] for l in fight if l in {'w': 4, 'p': 3, 'b': 2, 's': 1}])
    right_points = sum([{'m': 4, 'q': 3, 'd': 2, 'z': 1}[l] for l in fight if l in {'m': 4, 'q': 3, 'd': 2, 'z': 1}])
    if left_points > right_points:
        return 'Left side wins!'
    elif left_points < right_points:
        return 'Right side wins!'
    else:
        return "Let's fight again!"
