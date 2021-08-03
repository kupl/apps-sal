def find_ball(scales, ball_count):
    return find(scales, [*range(ball_count)])


def find(scales, balls):
    l = len(balls)
    if l == 1:
        return balls[0]
    l = -(l // -3)
    a, b, c = balls[:l], balls[l:l + l], balls[l + l:]
    v = scales.get_weight(a, b)
    if v == -1:
        return find(scales, a)
    if v == 1:
        return find(scales, b)
    return find(scales, c)
