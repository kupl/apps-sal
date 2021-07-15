# write the function is_anagram
def is_anagram(test, original):
    if sorted(test.lower()) == sorted(original.lower()):
        return True
    else:
        return False
    
# had to look up new function for me: sorted, had to work the turkey through with .lower

