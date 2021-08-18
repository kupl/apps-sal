def find_digit(num, nth):
    num_str = str(num)
    if nth < 1:
        return -1
    elif nth > len(num_str):
        return 0
    else:
        return int(num_str[-1 * nth])
