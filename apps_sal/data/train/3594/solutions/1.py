from collections import Counter

def is_isogram(word):
    try:
        return len(set(Counter(filter(str.isalpha, word.lower())).values())) == 1
    except AttributeError:
        return False
