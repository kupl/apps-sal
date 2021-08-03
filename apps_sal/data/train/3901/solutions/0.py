def check_digit(n, idx1, idx2, digit):
    return str(digit) in str(n)[idx1:idx2 + 1] + str(n)[idx2:idx1 + 1]
