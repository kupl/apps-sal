def compare(s1, s2):
    if s1 is None or not s1.isalpha():
        s1 = ''
    if s2 is None or not s2.isalpha():
        s2 = ''
    x1 = sum([ord(i.upper()) for i in s1])
    x2 = sum([ord(i.upper()) for i in s2])
    return x1 == x2
