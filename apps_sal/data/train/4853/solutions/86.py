def double_char(s):
    
    returnString = ""
    i = 0
    
    while i < len(s):
        returnString = returnString + s[i] + s[i]
        i+= 1
    
    return returnString
