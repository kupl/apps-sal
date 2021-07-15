def is_anagram(test, original):
    test = sorted(test.lower())
    original = sorted(original.lower())
    if original == test:
        return True
    return False
