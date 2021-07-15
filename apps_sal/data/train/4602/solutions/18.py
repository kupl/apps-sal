def is_anagram(test, original):
    return set(original.lower()) == set(test.lower()) if len(test) == len(original) else False
