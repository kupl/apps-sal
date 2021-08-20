def is_anagram(test, original):
    test = test.upper()
    original = original.upper()
    if sorted(test) == sorted(original):
        return True
    else:
        return False
