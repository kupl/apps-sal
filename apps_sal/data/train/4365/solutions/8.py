from collections import Counter

def is_isogram(string):
    for x in Counter(string.lower()).values():
        if x > 1:
            return False
    return True
