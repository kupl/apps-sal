def is_anagram(test, original):
    test = test.lower()
    original = original.lower()
    for char in test:
        if char in original:
            original = original.replace(char, '', 1)
        else: return False
    if len(original) == 0: return True
    else: return False
