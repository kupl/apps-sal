def two_decimal_places(number):
    string = str(number)
    n = string.find('.')
    return float(string[0:n+3])
