import re


def contamination(text, char):
    return re.sub(".", char, text)
