def reverseWords(s):
    str_split = s.split(" ")
    
    string = ""
    
    for i in str_split:
        
        string = i + " " + string
    
    return string.rstrip()

