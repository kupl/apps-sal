def ball_probability(balls):
    (balls, draw, repl) = balls
    (b1, l1) = (balls.count(draw[0]), len(balls))
    if b1 == 0:
        return 0
    b2 = balls.count(draw[1]) if draw[0] != draw[1] else b1 + repl - 1
    l2 = l1 + repl - 1
    return round(b1 / l1 * b2 / l2, 3)
