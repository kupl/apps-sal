def is_anagram(test, original):
    list_test = []
    list_original = []
    for i in test.lower():
        list_test += i
    for i in original.lower():
        list_original += i
    if  len(list_test) == len(list_original):
        list_test.sort()
        list_original.sort()
        if list_test == list_original:
            return True
        else:
            return False
    else:
        return False
