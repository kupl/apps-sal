def lowercase_count(strng):
    import re
    result = ''
    match = re.findall('[a-z]', strng)
    result = ''.join(match)
    return len(result)
