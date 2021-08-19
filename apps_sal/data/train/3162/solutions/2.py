def compare(s1, s2):
    if not s1 or not s1.isalpha():
        s1 = ''
    if not s2 or not s2.isalpha():
        s2 = ''
    return sum((ord(x) for x in s1.upper())) == sum((ord(y) for y in s2.upper()))
