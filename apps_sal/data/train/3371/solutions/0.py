import re


def signed_eight_bit_number(number):
    return bool(re.match('(0|-128|-?([1-9]|[1-9]\\d|1[01]\\d|12[0-7]))\\Z', number))
