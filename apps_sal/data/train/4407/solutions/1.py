def no_ifs_no_buts(a, b):
    return ['%d is smaller than %d', '%d is equal to %d', '%d is greater than %d'][int(a >= b) + int(a > b)] % (a, b)
