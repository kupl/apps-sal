POWERS = {c: i for (i, c) in enumerate('wpbs zdqm', -4)}


def alphabet_war(fight):
    stroke = sum((POWERS[c] for c in fight if c != ' ' and c in POWERS))
    return ['Left side wins!', "Let's fight again!", 'Right side wins!'][(stroke >= 0) + (stroke > 0)]
