import re


def reverseWords(str):
    return ''.join(re.split('(\\s+)', str)[::-1])
