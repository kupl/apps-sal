# write the function is_anagram
def is_anagram(test, original):
    t = list(test.lower())
    to = ''.join(sorted(t))
    o = list(original.lower())
    oo = ''.join(sorted(o))
    if to == oo:
        return True
    else:
        return False
