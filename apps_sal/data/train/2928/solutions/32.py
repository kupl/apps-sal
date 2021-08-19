def alphabet_war(fight):
    left_side = ('s', 'b', 'p', 'w')
    left_score = 0
    right_side = ('z', 'd', 'q', 'm')
    right_score = 0
    for c in fight:
        if c in left_side:
            left_score += left_side.index(c) + 1
        elif c in right_side:
            right_score += right_side.index(c) + 1
    return 'Right side wins!' if right_score > left_score else 'Left side wins!' if left_score > right_score else "Let's fight again!"
