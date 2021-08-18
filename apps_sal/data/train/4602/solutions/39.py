def is_anagram(test, original):
    t = sorted(test.lower())
    o = sorted(original.lower())
    if t == o:
        return True
    else:
        return False
