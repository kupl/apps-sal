def is_anagram(test, original):
    x = list(test.lower())
    y = list(original.lower())
    x = sorted(x)
    y = sorted(y)
    if x == y:
        return True
    else:
        return False
