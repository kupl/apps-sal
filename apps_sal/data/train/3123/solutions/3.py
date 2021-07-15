import re

def count_repeats(str):
    return len(str) - len(re.sub(r'(.)\1+', r'\1', str))
