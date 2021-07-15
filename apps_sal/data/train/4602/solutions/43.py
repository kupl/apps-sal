# write the function is_anagram
def is_anagram(test, original):
    first = [i.lower() for i in test]
    second = [i.lower() for i in original]
    return sorted(first) == sorted(second)
