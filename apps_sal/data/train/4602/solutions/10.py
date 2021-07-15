def is_anagram(test, original):
    if len(test) != len(original):
        return False
    for l in test.lower():
        if l not in original.lower():
            return False
    return True
