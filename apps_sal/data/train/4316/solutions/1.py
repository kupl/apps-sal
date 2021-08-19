import re


def reverse_by_center(s):
    half = len(s) // 2
    return re.sub('(.{%s})(.?)(.{%s})' % (half, half), '\\3\\2\\1', s)
