def find_ball(scales, n=8):
    balls = list(range(n))
    while len(balls) > 1:
        left, right, out = balls[::3], balls[1::3], balls[2::3]
        if len(balls) % 3 == 1:
            out.append(left.pop())
        balls = [left, out, right][scales.get_weight(left, right) + 1]
    return balls.pop()
