import re
def lowercase_count(strng):
    
    regex = r'[a-z]'

    return len(re.findall(regex, strng))
