def get_value(s):
    if not s or not s.isalpha():
        return 0
    return sum(ord(c) for c in s.upper())

def compare(s1,s2):
    return get_value(s1)==get_value(s2)
