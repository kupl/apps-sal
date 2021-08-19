def is_anagram(test, original):
    test = test.lower().replace(' ', '')
    original = original.lower().replace(' ', '')
    if len(test) != len(original):
        return False
    for letter in test:
        if letter not in original:
            return False
    for letter in original:
        if letter not in test:
            return False
    return True
