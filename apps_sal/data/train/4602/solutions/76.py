def is_anagram(test, original):
    test = list(test.lower())
    test.sort()
    original = list(original.lower())
    original.sort()
    if original != test or len(test) != len(original):
        return False
    else:
        return True
