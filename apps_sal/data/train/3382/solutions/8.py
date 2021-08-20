import re


def lowercase_count(st):
    return len(re.sub('[^a-z]*', '', st))
