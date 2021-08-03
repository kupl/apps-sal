def compare(s1, s2):
    try:
        if s1.isalpha() != True:
            s1 = ''
    except:
        s1 = ''
    try:
        if s2.isalpha() != True:
            s2 = ''
    except:
        s2 = ''
    return sum([ord(i) for i in s1.upper()]) == sum([ord(i) for i in s2.upper()])
