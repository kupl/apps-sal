def sum_digits(number):
    chars = list(str(number))
    digits = [int(char) for char in chars if char.isdigit()]
    return sum(digits)

