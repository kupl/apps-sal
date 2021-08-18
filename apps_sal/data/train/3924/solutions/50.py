import re


def reverse_words(text):
    arr = re.split(r'(\s+)', text)
    reverse = [i[::-1]for i in arr]
    finished = ''.join(reverse)
    return finished
