def compare(s1, s2):
    if s1 == None or [x for x in s1 if x.isalpha() == False]:
        s1 = ''
    if s2 == None or [x for x in s2 if x.isalpha() == False]:
        s2 = ''
    return sum((ord(x.upper()) for x in s1)) == sum((ord(x.upper()) for x in s2))
