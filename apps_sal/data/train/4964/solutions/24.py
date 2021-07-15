def is_uppercase(inp):
    
    count = 0
    
    letters = list(inp)
    for x in letters:
        if count < len(letters):
            if x.islower():
                return False
            if x.isupper():
                count +=1
                if x.islower():
                    return False
    return True
