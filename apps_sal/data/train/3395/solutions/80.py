def remove_duplicate_words(s):
    
    split_string = s.split()
    
    new_string = ""
    
    for word in split_string:
        if word not in new_string:
            new_string+=word + " "
        else:
            continue
            
    return new_string.rstrip()
    

