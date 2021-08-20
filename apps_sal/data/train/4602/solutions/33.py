def is_anagram(test, original):
    if len(test) != len(original):
        return False
    a = sorted(test.lower())
    b = sorted(original.lower())
    if a == b:
        return True
    else:
        return False
