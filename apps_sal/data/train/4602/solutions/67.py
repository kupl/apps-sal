def is_anagram(test, original):
    test = test.lower()
    original = original.lower()
    new_test = list(test)
    new_original = list(original)
    new_test.sort()
    new_original.sort()
    if new_test == new_original:
        return True
    return False
    pass
