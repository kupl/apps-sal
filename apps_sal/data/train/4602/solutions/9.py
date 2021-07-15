# write the function is_anagram
def is_anagram(test, original):
  #index = 0

    go = len(test) == len(original)

    arr = []

    if go:
    #print(True)
        for i in test:
            arr.append(i.lower() in original.lower()) # [True, True, False, ...]
    
        return False not in arr # Condition passed => True.  
    else:
        return False
