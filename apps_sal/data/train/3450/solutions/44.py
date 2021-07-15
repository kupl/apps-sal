def array(string):
    #Had to add the replace() since some of the input test strings have spaces
    #in addition to commas
    
    #step1: Convert the input string to list of characters, removing spaces
    #and splitting based on comma
    l = string.replace(' ','').split(',')
    
    #step 2: return all the chars in list, except first and list, joined using ' '
    #check for len of list and return None if < 3
    return ' '.join(l[1:-1]) if len(l) >= 3 else None
