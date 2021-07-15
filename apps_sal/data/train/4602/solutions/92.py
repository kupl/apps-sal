# write the function is_anagram
def is_anagram(test, original):
    return len(test) == len(original) and all([i in original.lower() for i in test.lower()])
