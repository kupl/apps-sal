def is_anagram(test, original):
    if len(test) != len(original):
        return False
    elif sorted(test.casefold()) == sorted(original.casefold()):
        return True
    else:
        return False
