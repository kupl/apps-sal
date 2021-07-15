def double_char(s):
    
    #start with an empty string
    x = ""
    
    ##loop across string s, and add each letter twice to empty string x
    for i in range(len(s)):
        x = x+s[i]+s[i]
    return x

    pass
