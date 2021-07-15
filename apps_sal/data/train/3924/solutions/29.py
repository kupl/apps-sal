import re

def reverse_words(text):
    return re.sub(r'([^ ]+)', lambda x: x.group()[::-1], text)
