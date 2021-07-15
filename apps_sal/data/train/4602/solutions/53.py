def is_anagram(test, original):
    if len(test) == len(original):
        
        test = test.lower()
        original = original.lower()
        
        for i in test:
            if original.find(i) == -1:
                return False
            else:
                test.replace(i, "")
                original.replace(i, "")
    else:
        return False
    
    return True
