import re
def buy_newspaper(s1, s2):
    if not set(s2) <= set(s1):
        return -1
    regex = ''.join(c + '?' for c in s1)
    return len([match for match in re.findall(regex, s2) if match])
