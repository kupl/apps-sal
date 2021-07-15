import re
def lowercase_count(string):
    return len(re.findall('[a-z]',string))
