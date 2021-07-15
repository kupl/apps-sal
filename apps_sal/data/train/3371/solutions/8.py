import re

def signed_eight_bit_number(number):
    return bool(re.fullmatch(r"(-?(1(([2][0-7])|([01]\d))|[1-9][0-9]))|\d|-[1-9]|-128", number))
