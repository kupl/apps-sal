def is_anagram(test, original):
    a = sorted(test.lower())
    b = sorted(original.lower())
    c = ''.join(a)
    d = ''.join(b)
    if c == d:
        return True
    else:
        return False
