import re


def spin_words(sentence):
    return re.sub('\\w{5,}', lambda w: w.group(0)[::-1], sentence)
