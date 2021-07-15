# write the function is_anagram
def is_anagram(test, original):
    return True if sorted([letter for letter in test.lower()]) == sorted([letter for letter in original.lower()]) else False
    

