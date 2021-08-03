def alphabet_war(fight):
    left = '0sbpw'
    right = '0zdqm'
    l = sum(left.index(i) for i in fight if i in left)
    r = sum(right.index(i) for i in fight if i in right)
    if r == l:
        return "Let's fight again!"
    if l > r:
        return "Left side wins!"
    return "Right side wins!"
