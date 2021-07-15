import string
def to_alternating_case(s):
    ans = ''
    for c in s:
        if c in string.ascii_lowercase:
            ans += c.upper()
        elif c in string.ascii_uppercase:
            ans += c.lower()
        else:
            ans += c
    return ans
