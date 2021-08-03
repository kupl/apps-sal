def max_multiple(divisor, bound):
    valid_list = []
    for n in range(1, bound + 1):
        if n % divisor == 0:
            valid_list.append(n)
    valid_list = sorted(valid_list)
    return valid_list[-1]
