def elevator(left, right, call):

    diff_left = abs(left - call)

    diff_right = abs(right - call)

    if diff_left >= diff_right:

        return "right"

    if diff_left < diff_right:

        return "left"
