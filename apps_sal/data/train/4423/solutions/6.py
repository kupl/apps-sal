from collections import Counter


def ball_probability(balls):
    c = Counter(balls[0])
    (b1, b2) = balls[1]
    if balls[2]:
        return round(c[b1] / len(balls[0]) * c[b2] / len(balls[0]), 3)
    else:
        return round(c[b1] / len(balls[0]) * (c[b2] - 1 if b1 == b2 else c[b2]) / (len(balls[0]) - 1), 3)
