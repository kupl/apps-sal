def is_anagram(test, original):
    test = test.lower()
    original = original.lower()
    if len(test) != len(original):
        return False
    for x in test:
        if test.count(x) == original.count(x):
            continue
        else:
            return False
    return True
