def compare(s1, s2):
    if not s1 or s1.isalpha() is False:
        s1 = ''
    if not s2 or s2.isalpha() is False:
        s2 = ''
    return sum([ord(c) for c in s1.upper()]) == sum([ord(c) for c in s2.upper()])
