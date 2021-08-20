def is_anagram(test, original):
    new_test = test.lower()
    new_original = original.lower()
    sortedTest = sorted(new_test)
    sortedOriginal = sorted(new_original)
    for letters in new_test:
        if letters in new_original and len(new_test) == len(new_original) and (sortedOriginal == sortedTest):
            return True
        else:
            return False
