def lowercase_count(strng):
    letters = str(strng)
    lowercase = 0 
    for i in letters: 
        if i.islower():
            lowercase += 1
            
    return lowercase

