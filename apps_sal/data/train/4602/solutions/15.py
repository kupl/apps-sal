# write the function is_anagram
def is_anagram(test, original):
    return sorted(list(test.lower())) == sorted(list(original.lower()))
