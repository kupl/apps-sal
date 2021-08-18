def balanced_num(number):

    num_len = len(str(number))

    left_tot = 0
    right_tot = 0

    if num_len <= 2:
        return "Balanced"
    else:
        if num_len % 2 == 1:
            width = num_len // 2
        else:
            width = (num_len // 2) - 1

        left = str(number)[:width]
        for pos_l, left_sum in enumerate(left):
            left_tot += int(left_sum)

        right = str(number)[-1 * width:]
        for pos_r, right_sum in enumerate(right):
            right_tot += int(right_sum)

    if left_tot == right_tot:
        return "Balanced"
    else:
        return "Not Balanced"
