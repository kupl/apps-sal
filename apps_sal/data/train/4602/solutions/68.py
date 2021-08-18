def is_anagram(test, original):
    return set(test.upper()) == set(original.upper()) and len(test) == len(original)
