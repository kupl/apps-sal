def is_anagram(test, original):
    test = test.lower()
    original = original.lower()
    newList = [ord(c) for c in test]
    newList.sort()
    newList2 = [ord(b) for b in original]
    newList2.sort()
    if newList == newList2:
        return True
    else:
        return False
