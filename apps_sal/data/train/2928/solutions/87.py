def alphabet_war(fight):
    chars = list(fight)
    left = 4 * chars.count('w') + 3 * chars.count('p') + 2 * chars.count('b') + 1 * chars.count('s')
    right = 4 * chars.count('m') + 3 * chars.count('q') + 2 * chars.count('d') + 1 * chars.count('z')
    if left > right:
        return "Left side wins!"
    elif left < right:
        return "Right side wins!"
    else:
        return "Let's fight again!"
