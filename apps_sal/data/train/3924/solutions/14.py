import re
import textwrap


def reverse_words(text):
    text = re.split('([\\s,;()]+)', text)
    separator = ''
    for (n, string) in enumerate(text):
        text[n] = list(text[n])
        text[n].reverse()
        text[n] = separator.join(text[n])
    text = separator.join(text)
    return text
