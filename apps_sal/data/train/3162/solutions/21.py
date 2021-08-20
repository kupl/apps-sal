import re


def compare(s1, s2):
    if s1 is None or s1 is [] or re.search('[^a-zA-Z]', s1):
        s1 = []
    if s2 is None or s2 is [] or re.search('[^a-zA-Z]', s2):
        s2 = []
    return True if s2 == s1 else True if sum((ord(x.upper()) for x in s1)) == sum((ord(x.upper()) for x in s2)) else False
