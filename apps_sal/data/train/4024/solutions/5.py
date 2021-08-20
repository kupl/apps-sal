import re


def special_number(number):
    return 'Special!!' if re.match('^[0-5]+$', str(number)) else 'NOT!!'
