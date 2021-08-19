# write the function is_anagram
def is_anagram(test, original):
    a = sorted(test.lower())
    b = sorted(original.lower())
    if a == b:
        c = True
    else:
        c = False
    return c
