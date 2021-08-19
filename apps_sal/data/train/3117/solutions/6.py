import re


def solve(s):
    return len(max(re.findall('[aeiou]+', s), key=len, default=''))
