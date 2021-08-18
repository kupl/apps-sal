def is_anagram(test, original):
    test = test.lower()
    original = original.lower()
    t = list(test)
    o = list(original)
    t.sort()
    o.sort()
    return t == o
