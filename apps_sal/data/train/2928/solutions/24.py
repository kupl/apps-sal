def alphabet_war(fight):
    points = 'mqdz*sbpw'
    score = sum((i * fight.count(p) for (i, p) in enumerate(points, -4)))
    if score == 0:
        return "Let's fight again!"
    return ['Left', 'Right'][score < 0] + ' side wins!'
