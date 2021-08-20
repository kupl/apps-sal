def solve(count, ball_number):
    """
    Return the position of the `ball_number` after the game with `count` balls

    :param count: Number of balls
    :type count: int
    :param ball_number: Number of ball to be found in the end
    :type ball_number: int
    :return: Return the index of the ball `ball_number` at the end of the game
    :rtype: int
    """
    assert isinstance(count, int)
    assert isinstance(ball_number, int)
    balls = list(range(count))
    for idx in range(count):
        balls = balls[:idx] + balls[idx:][::-1]
    return balls.index(ball_number)
