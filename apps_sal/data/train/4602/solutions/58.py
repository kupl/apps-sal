def is_anagram(test, original):
    return sorted([n.lower() for n in test]) == sorted([n.lower() for n in original])
