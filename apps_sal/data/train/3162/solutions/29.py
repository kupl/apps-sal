def compare(s1,s2):
    try:
        if not s1.isalpha():
            s1 = ''
    except AttributeError:
        s1 = ''
    try:
        if not s2.isalpha():
            s2 = ''
    except AttributeError:
        s2 = ''
    summ = 0
    for i in s1.upper():
        summ += ord(i)
    for i in s2.upper():
        summ -= ord(i)
    return summ ==0
