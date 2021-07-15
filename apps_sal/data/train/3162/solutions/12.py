def count_value(s):
    return sum([ord(c) for c in s.upper()]) if s and s.isalpha() else 0

def compare(s1,s2):
    return count_value(s1) == count_value(s2)
