import re


def timed_reading(max_length, text):
    return sum(len(i) <= max_length for i in re.findall('\w+', text))
