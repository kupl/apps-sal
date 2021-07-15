# write the function is_anagram
def is_anagram(test, original):
    test = test.lower()
    original = original.lower()
    #transform string to list in order to sort by alphabet
    new_test = list(test)
    new_original = list(original) 
    #sort 
    new_test.sort()
    new_original.sort()
    
    if(new_test == new_original):
        return True
    return False
    pass
