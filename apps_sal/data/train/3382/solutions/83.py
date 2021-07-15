import re
def lowercase_count(strng):
    chars = re.findall("[a-z]", strng)
    return len(chars)
