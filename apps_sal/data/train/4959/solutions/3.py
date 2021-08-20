def find_ball(scales, ball_count):

    def find_number(numbers):
        length = len(numbers)
        if length == 1:
            return numbers[0]
        n = length // 3 + (length % 3 == 2)
        (left, right, remaining) = (numbers[:n], numbers[n:2 * n], numbers[2 * n:])
        result = scales.get_weight(left, right)
        if result < 0:
            return find_number(left)
        elif result > 0:
            return find_number(right)
        else:
            return find_number(remaining)
    return find_number(list(range(ball_count)))
