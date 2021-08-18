def is_anagram(test, original):
    test = [i.lower() for i in test]
    original = [j.lower() for j in original]
    test.sort()
    original.sort()
    return test == original
