def compare(s1, s2):
    if s1 is None:
        s1 = ''
    if s2 is None:
        s2 = ''
    for char in s1:
        if not char.isalpha():
            s1 = ''
    for char in s2:
        if not char.isalpha():
            s2 = ''
    res1 = sum((ord(x) for x in s1.upper()))
    res2 = sum((ord(x) for x in s2.upper()))
    return res1 == res2
