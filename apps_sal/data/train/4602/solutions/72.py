# write the function is_anagram
def is_anagram(test, original):
    test_l = list(test.lower())
    original_l = list(original.lower())
    test_l.sort()
    original_l.sort()
    if test_l == original_l:
        return(True)
    else:
        return(False)
