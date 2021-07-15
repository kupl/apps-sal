def solve(s):
    space_index=[i for i in range(len(s)) if s[i]==" "]    #find index of saces  
    s = ''.join(s.split())                                 #remove spaces
    s=s[::-1]                                              #reverse the string    
    for i in space_index:                                  #add spaces again to exactly same place before
        s = s[:i] + " " + s[i:]
    return s
