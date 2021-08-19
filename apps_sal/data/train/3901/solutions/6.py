def check_digit(number, index1, index2, digit):
    return str(digit) in str(number)[min(index1, index2):max(index1, index2) + 1]
