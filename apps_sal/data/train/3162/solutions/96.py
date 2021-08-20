def compare(s1, s2):
    if (not s1 or not s1.isalpha()) and (not s2 or not s2.isalpha()):
        return True
    if s1.isalpha() != s2.isalpha():
        return False
    return sum((ord(c) for c in s1.upper())) == sum((ord(c) for c in s2.upper()))
