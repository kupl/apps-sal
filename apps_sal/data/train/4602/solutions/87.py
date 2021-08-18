def is_anagram(test, original):
    sort1 = sorted(test.lower())
    sort2 = sorted(original.lower())
    if ''.join(sort2) == ''.join(sort1):
        return True
    else:
        return False
