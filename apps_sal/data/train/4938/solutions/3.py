from collections import Counter

def count_char(s, c):
    return Counter(s.lower())[c.lower()]
