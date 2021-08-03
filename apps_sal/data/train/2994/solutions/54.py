def find_digit(num, nth):
    if nth <= 0:
        return -1
    num_mod = str(abs(num))[::-1]
    if nth > len(num_mod):
        return 0
    else:
        return int(num_mod[nth - 1])
