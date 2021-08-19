def longest_slide_down(pyramid):
    if len(pyramid) == 1:
        return pyramid[0][0]
    (left, current) = (pyramid[:-1], pyramid[-1])
    pair_sum_g = map(max, zip(current[:-1], current[1:]))
    for (i, x) in enumerate(pair_sum_g):
        left[-1][i] += x
    return longest_slide_down(left)
