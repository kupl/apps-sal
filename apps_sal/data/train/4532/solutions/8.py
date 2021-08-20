from re import match
from math import log10


def validate_code(code):
    return 0 < code // 10 ** int(log10(code)) < 4
    return bool(match('\\A[1-3]', str(code)))
