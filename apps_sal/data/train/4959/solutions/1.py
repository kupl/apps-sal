def find_ball(scales, ball_count):
    balls = range(ball_count)

    while (len(balls) > 1):
        x = len(balls) / 3 + (len(balls) % 3 > 0)
        j, k, l = balls[:x], balls[x:x * 2], balls[x * 2:]
        balls = [l, k, j][scales.get_weight(j, k)]

    return balls[0]
