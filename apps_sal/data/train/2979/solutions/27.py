import re

def get_age(age):
    return int(''.join(re.findall(r'\d', age)))
