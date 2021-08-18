def is_anagram(test, original):
    if len(test) != len(original):
        return False
    return sorted(test.lower()) == sorted(original.lower())
