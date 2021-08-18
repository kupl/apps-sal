def is_anagram(test, original):
    if len(test) == len(original):
        test = test.lower()
        original = original.lower()
        count = 0

        for char in test:
            if char in original:
                count += 1

        if count == len(test):
            return True
        else:
            return False
    else:
        return False
