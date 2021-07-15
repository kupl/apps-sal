# write the function is_anagram
def is_anagram(test, original):
    n = len(original)
    if n != len(test):
        return False
    
    counterTest = [0] * 255
    counterOrig = [0] * 255
    
    for i in range(n):
        counterTest[ord(test[i].lower())] += 1
        counterOrig[ord(original[i].lower())] += 1
        
    return True if "".join(map(str, counterTest)) == "".join(map(str, counterOrig)) else False
