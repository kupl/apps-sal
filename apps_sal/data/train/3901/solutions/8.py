def check_digit(number, index1, index2, digit):
    left = min([index1, index2])
    right = max([index1, index2])
    return True if str(digit) in str(number)[left:right+1] else False
