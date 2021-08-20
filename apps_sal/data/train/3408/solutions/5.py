def add_check_digit(number):
    checksum = sum((int(d) * (2, 3, 4, 5, 6, 7)[i % 6] for (i, d) in enumerate(reversed(number))))
    checkdigit = 11 - checksum % 11
    return number + str({11: 0, 10: 'X'}.get(checkdigit, checkdigit))
