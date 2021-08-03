def compare(s1, s2):
    s1 = s1 if s1 and s1.isalpha() else []
    s2 = s2 if s2 and s2.isalpha() else []
    return sum(ord(x.upper()) for x in s1) == sum(ord(x.upper()) for x in s2)
