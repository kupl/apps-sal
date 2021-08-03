def compare(s1, s2):
    if s1 is None:
        s1 = ''
    if s2 is None:
        s2 = ''
    for c in s1:
        if not c.isalpha():
            s1 = ''
            break
    for c in s2:
        if not c.isalpha():
            s2 = ''
            break
    return sum(ord(c.upper()) for c in s1) == sum(ord(c.upper()) for c in s2)
