import re


def timed_reading(max_length, text):
    return len(re.findall('\\b\\w{1,%s}\\b' % str(max_length), text)) if max_length >= 2 else 0
