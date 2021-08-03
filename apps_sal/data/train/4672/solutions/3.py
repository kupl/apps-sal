import re


def AlphaNum_NumAlpha(string):
    def f(x): return str(ord(x) - ord('a') + 1) if x.isalpha() else chr(ord('a') + int(x) - 1)
    return ''.join([f(x) for x in re.findall(r'\d{1,2}|[a-z]', string)])
