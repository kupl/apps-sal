def find_the_ball(start, swaps):
    """ Where is the ball? """
    ball = start
    for (a, b) in swaps:
        if ball == a:
            ball = b
        elif ball == b:
            ball = a
    return ball
