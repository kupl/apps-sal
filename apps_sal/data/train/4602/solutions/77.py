def is_anagram(test, original):
    if len(test) != len(original):
        return False
    test = sorted(test.lower())
    original = sorted(original.lower())
    for i in range(len(test)):
        if test[i] != original[i]:
            return False
    return True 
