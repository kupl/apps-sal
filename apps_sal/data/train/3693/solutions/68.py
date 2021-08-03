def make_negative(number):
    a = list(str(number))
    return -1 * number if a[0] != "-" else number
