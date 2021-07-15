# write the function is_anagram
def is_anagram(test, original):
    return sorted(test.upper()) == sorted(original.upper())
