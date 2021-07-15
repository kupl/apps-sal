# write the function is_anagram
def is_anagram(test, original):
    
    test = test.lower()
    original = original.lower()
    
    testcount = 0
    for i in test:
        if i in original:
            testcount += 1
            
    originalcount = 0
    for i in original:
        if i in test:
            originalcount += 1
            
    if testcount == originalcount and testcount == len(test) and originalcount == len(original):
        return True
    else:
        return False

