# write the function is_anagram
def is_anagram(test, original):
    if sorted(test.lower()) == sorted(original.lower()):
        return True
    else:
        return False
