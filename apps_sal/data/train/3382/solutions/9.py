import re


def lowercase_count(text):
    return len(re.findall('[a-z]', text))
