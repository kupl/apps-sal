import re

def double_check(s):
    return bool(re.search(r'(.)\1', s.lower()))
