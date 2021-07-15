def alphabet_war(fight):
    left = {c: i for i, c in enumerate("sbpw", 1)}
    right = {c: i for i, c in enumerate("zdqm", 1)}
    battle = sum(left.get(c, 0) - right.get(c, 0) for c in fight.lower())
    if battle > 0:
        return "Left side wins!"
    elif battle < 0:
        return "Right side wins!"
    else:
        return "Let's fight again!"
