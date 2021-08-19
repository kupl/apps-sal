def ball_probability(balls):
    (l, selection, replaced) = balls
    (a, b) = selection
    prob = l.count(a) * (l.count(b) + (0 if replaced or a != b else -1)) / (len(l) * (len(l) + (0 if replaced else -1)))
    return round(prob, 3)
