def pig_latin(s):
    if not s.isalpha():
        return None
    s = s.lower()
    if s.startswith(('a', 'e', 'i', 'o', 'u')):
        s += 'w'
        i = 0
    else:
        i = next((i for i, c in enumerate(s) if c in 'aeiou'), 0)
    return s[i:] + s[:i] + 'ay'

