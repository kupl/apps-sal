def is_anagram(test, original):
    test = list(test.lower())
    original = list(original.lower())
    if sorted(test) == sorted(original):
        return True
    else:
        return False
