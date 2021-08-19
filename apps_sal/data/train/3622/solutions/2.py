import re


def validate_usr(str):
    return bool(re.match('^[a-z\\d_]{4,16}$', str))
