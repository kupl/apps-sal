import re


def reverse_words(str):
    return re.sub('\\S+', lambda w: w.group(0)[::-1], str)
