# write the function is_anagram
def is_anagram(test, original):
    test_list = [letter1 for letter1 in test.lower()]
    orig_list = [letter2 for letter2 in original.lower()]
    
    if sorted(test_list) == sorted(orig_list):
        return True    
    else:
        return False
        
    
        


