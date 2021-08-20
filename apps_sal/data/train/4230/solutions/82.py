import re


def reverse_letter(string):
    regex = re.compile('[^a-z]')
    reg = regex.sub('', string)
    reverse_word = reg[::-1]
    return reverse_word
