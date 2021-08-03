def ball_probability(balls):
    bag, t, r = balls
    a, b = (bag.count(i) for i in t)
    m = len(bag)
    return round(1.0 * a * (b if r or t[0] != t[1] else b - 1) / m / (m if r else m - 1), 3)
