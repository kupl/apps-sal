def two_decimal_places(number):
    number = str(number)
    return float(number[:number.index('.') + 3])
