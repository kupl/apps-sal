def compare(s1,s2):
    if s1 and s2:
        if s1.isalpha() and s2.isalpha():
            return sum([ord(x) for x in s1.upper()])==sum([ord(x) for x in s2.upper()])
        elif s1.isalpha() or s2.isalpha(): return False
    return True
