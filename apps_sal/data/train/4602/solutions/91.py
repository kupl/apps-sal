def is_anagram(test, original):

    letters_original=sorted(list(original.upper()))
    letters_test=sorted(list(test.upper()))

    return letters_original==letters_test
