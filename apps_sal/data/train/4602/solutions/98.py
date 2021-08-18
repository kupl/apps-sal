def is_anagram(test, original):
    original_list = list(original.lower())
    test_list = list(test.lower())
    original_list.sort()
    test_list.sort()
    a = "".join(test_list)
    b = "".join(original_list)
    return a == b
