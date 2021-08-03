def is_anagram(test, original):
    if sorted(test.lower()) == sorted(original.lower()):
        return True
    elif test != original:
        return False
