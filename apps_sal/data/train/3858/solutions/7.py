import re


def unscramble_eggs(s):
    return re.sub('(?i)([^\\Waeiou_])egg', '\\1', s)
