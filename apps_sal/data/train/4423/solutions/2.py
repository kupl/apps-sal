def ball_probability(balls):
    size = len(balls[0])
    if not balls[2]:
        p1 = balls[0].count(balls[1][0])
        p2 = p1 - 1 if balls[1][0] == balls[1][1] else balls[0].count(balls[1][1])
        return round(p1 * p2 / (size * (size - 1)), 3)
    return round(balls[0].count(balls[1][0]) * balls[0].count(balls[1][1]) / size ** 2, 3)
