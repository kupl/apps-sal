import re
SIGNED_BYTE_PATTERN = re.compile('\n    \\A\n    (?:\n        0 |\n        -? (?:\n            1 (?:\n                [01] \\d? |\n                2 [0-7]? |\n                [3-9] )? |\n            [2-9] \\d? ) |\n        -128 )\n    \\Z\n', re.X)


def signed_eight_bit_number(number):
    return bool(SIGNED_BYTE_PATTERN.search(number))
