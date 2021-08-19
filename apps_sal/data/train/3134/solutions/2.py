import re


def is_valid(identifier):
    return bool(re.fullmatch('[a-z_$][\\w$]*', identifier, flags=re.IGNORECASE))
