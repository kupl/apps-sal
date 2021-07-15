def is_anagram(test, original):
    for i in test.lower():
        if i in original.lower() and len(test) == len(original):
            continue
        else:
            return False
    return True
