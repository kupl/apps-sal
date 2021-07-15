import re

SIGNED_BYTE_PATTERN = re.compile(r'''
    \A
    (?:
        0 |
        -? (?:
            1 (?:
                [01] \d? |
                2 [0-7]? |
                [3-9] )? |
            [2-9] \d? ) |
        -128 )
    \Z
''', re.X)


def signed_eight_bit_number(number):
    return bool(SIGNED_BYTE_PATTERN.search(number))

