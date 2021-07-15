def is_anagram(test, original):
    test_list = []
    original_list = []
    for i in test.lower():
        test_list.append(i)
    for i in original.lower():
        original_list.append(i)
    test_list.sort()
    original_list.sort()
    print(test_list)
    print(original_list)
    if test_list == original_list:
        return True
    else:
        return False
