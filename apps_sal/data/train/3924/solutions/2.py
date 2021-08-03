import re


def reverse_words(str):
    return re.sub(r'\S+', lambda w: w.group(0)[::-1], str)
