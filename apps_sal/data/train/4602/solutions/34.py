def is_anagram(test, original):

    sorted_test = sorted(list(test.lower()))
    sorted_original = sorted(list(original.lower()))

    return sorted_test == sorted_original
