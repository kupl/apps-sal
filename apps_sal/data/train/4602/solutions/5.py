def is_anagram(test, original):
    test_dict, original_dict = {}, {}
    for i in test.lower():
        test_dict[i] = test_dict.get(i, 0) + 1
    for i in original.lower():
        original_dict[i] = original_dict.get(i, 0) + 1

    return test_dict == original_dict
