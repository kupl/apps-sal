def repeat_it(string,n):
    if n==0:    
        return ''
    for i in range(n):
        if isinstance(string, str)==True:
            return string*n
      
        else:    
            return "Not a string"

