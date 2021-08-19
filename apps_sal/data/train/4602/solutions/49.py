def is_anagram(test, original):
    if len(test) != len(original):
        return False
    else:
        test = test.lower()
        original = original.lower()
        counter_original = [0] * 26
        counter_test = [0] * 26
        for i in test:
            counter_test[ord(i) - 97] += 1
        for i in original:
            counter_original[ord(i) - 97] += 1
    return counter_test == counter_original
