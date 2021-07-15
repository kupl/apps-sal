import re

excluded = re.compile(r'\b(a[ts]?|the|o[nf]|upon|in)\b')
non_char = re.compile(r'[^a-z]+')

def word_count(s):
    return len(re.sub(excluded, '', re.sub(non_char, ' ', s.lower())).split())
