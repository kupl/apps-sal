import re


def timed_reading(max_length, text):
    return sum((len(m.group()) <= max_length for m in re.finditer('\\w+', text)))
