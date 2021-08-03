import re


def reverser(sentence):
    return ''.join(i[::-1] for i in re.split(r'(\s+)', sentence))
