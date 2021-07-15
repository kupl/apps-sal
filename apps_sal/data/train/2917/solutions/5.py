import re

def distinct_digit_year(year):
    return year + 1 if re.match(r'(?:([0-9])(?!.*\1)){4}', str(year + 1)) else distinct_digit_year(year + 1)
