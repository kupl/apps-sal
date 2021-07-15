def is_anagram(test, original):
    test = test.lower()
    original = original.lower()
    for x in range(len(test)):
        if test.count(test[x]) != original.count(test[x]):
            return False
    for x in range(len(original)):
        if test.count(original[x]) != original.count(original[x]):
            return False
    return True
