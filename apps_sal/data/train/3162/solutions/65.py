def compare(s1, s2):
    empty1 = s1 in [None, ""] or any(not c1.isalpha() for c1 in s1)
    empty2 = s2 in [None, ""] or any(not c2.isalpha() for c2 in s2)
    if empty1 == empty2 == True:
        return True
    if empty1 ^ empty2:
        return False
    return sum(ord(c1) for c1 in s1.upper()) == sum(ord(c2) for c2 in s2.upper())
