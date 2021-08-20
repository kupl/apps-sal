def alphabet_war(fight):
    (a, b) = ('sbpw', 'zdqm')
    (l, r) = (sum([a.find(x) + 1 for x in fight]), sum([b.find(y) + 1 for y in fight]))
    return 'Right side wins!' if l < r else 'Left side wins!' if r < l else "Let's fight again!"
