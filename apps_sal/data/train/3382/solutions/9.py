import re
def lowercase_count(text):
    return len(re.findall(r'[a-z]', text))
