def lowercase_count(strng):
    import re
    return len(re.findall(r'[a-z]', strng))
