import re


def get_age(age):
    return int(re.match(pattern='(?P<age_char>^\\d.)', string=age).group('age_char'))
