def no_ifs_no_buts(a, b):
    compare = {
        -1: " is smaller than ",
        0: " is equal to ",
        1: " is greater than "
    }
    return str(a) + compare[(a > b) - (a < b)] + str(b)
