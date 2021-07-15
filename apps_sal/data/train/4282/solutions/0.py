import re

def hungry_seven(arr):
    ss,s = '', ''.join(map(str,arr))
    while ss!=s:
        ss,s = s,re.sub(r'(7+)(89)',r'\2\1', s)
    return list(map(int,s))
