import re


def reverse_letter(string):
    return re.sub('[^a-z]', '', string[::-1])
