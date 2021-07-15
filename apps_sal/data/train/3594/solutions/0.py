from collections import Counter
import re

def is_isogram(word):
    if type(word) is not str or not word: return False
    return len(set( Counter(re.sub(r'[^a-z]', "", word.lower())).values() )) == 1
