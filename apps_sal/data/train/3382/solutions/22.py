def lowercase_count(strng):
    import re
    return len(re.findall('[a-z]', strng))
