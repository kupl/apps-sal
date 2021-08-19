def alphabet_war(fight):
    left = 0
    right = 0
    for x in fight:
        if x in 'wpbs':
            p1 = {'w': 4, 'p': 3, 'b': 2, 's': 1}
            left += p1.get(x)
        elif x in 'mqdz':
            p2 = {'m': 4, 'q': 3, 'd': 2, 'z': 1}
            right += p2.get(x)
    if left != right:
        return 'Left side wins!' if left > right else 'Right side wins!'
    else:
        return "Let's fight again!"
