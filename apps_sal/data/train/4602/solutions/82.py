def is_anagram(test, original):
    test_list = sorted(list(test.lower()))
    original_list = sorted(list(original.lower()))
    if test_list == original_list:
        return True
    if test_list != original_list:
        return False
