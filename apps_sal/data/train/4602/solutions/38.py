def is_anagram(test, original):
    test_set = sorted(test.lower())
    original_set = sorted(original.lower())
    if test_set == original_set:
        return True
    else:
        return False
