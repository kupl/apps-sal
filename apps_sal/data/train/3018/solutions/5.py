import re
excluded = re.compile('\\b(a[ts]?|the|o[nf]|upon|in)\\b')
non_char = re.compile('[^a-z]+')


def word_count(s):
    return len(re.sub(excluded, '', re.sub(non_char, ' ', s.lower())).split())
