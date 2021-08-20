def is_anagram(test, original):
    print(test, original)
    test = test.lower()
    original = original.lower()
    test = sorted(test)
    original = sorted(original)
    if test == original:
        return True
    else:
        return False
