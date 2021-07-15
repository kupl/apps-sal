# write the function is_anagram
def is_anagram(test, original):
    originalLower =[val for val in original.lower()]
    arr = test.lower();
    if(len(arr) != len(originalLower)):
        return False
    for element in arr:
        if (element not in originalLower):
            return False
        else:
            originalLower.remove(element)
    return True

