def check_digit(number, index1, index2, digit):
    (number, digit) = (str(number), str(digit))
    (index1, index2) = sorted((index1, index2))
    return digit in number[index1:index2 + 1]
